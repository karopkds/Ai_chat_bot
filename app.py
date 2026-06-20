import os
import sys
import traceback

from flask import Flask, request, jsonify
from flask_cors import CORS

def _find_project_root(start_dir: str) -> str:
    """Walk upward from app.py's location until we find the folder that
    contains both 'src' and 'models'. Makes this work whether app.py lives
    in the project root or was placed inside src/ by mistake."""
    current = os.path.abspath(start_dir)
    for _ in range(4):
        if os.path.isdir(os.path.join(current, "src")) and os.path.isdir(
            os.path.join(current, "models")
        ):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    # Fallback: assume app.py is already at the project root
    return os.path.abspath(start_dir)


PROJECT_ROOT = _find_project_root(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

import joblib
from preprocessing import preprocess
from stop_words_removal import remove_stopwords
from lemmatizer import lemmatize
from response_engine import get_response

CONFIDENCE_THRESHOLD = 0.60
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------
# Load model artifacts once at startup
# ---------------------------------------------------------------------------
model = None
vectorizer = None
label_encoder = None
load_error = None

try:
    model = joblib.load(os.path.join(MODELS_DIR, "model.pkl"))
    vectorizer = joblib.load(os.path.join(MODELS_DIR, "tfidf.pkl"))
    label_encoder = joblib.load(os.path.join(MODELS_DIR, "label_encoder.pkl"))
except Exception as e:  # noqa: BLE001
    load_error = str(e)
    print(f"[WARN] Could not load model artifacts: {load_error}")


# ---------------------------------------------------------------------------
# Groq fallback — isolated import so a missing/blank API key never crashes
# the known-intent path.
# ---------------------------------------------------------------------------
def ask_groq(question: str) -> str:
    try:
        from groq import Groq

        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            # Fallback to config.py for local dev convenience.
            try:
                from config import GEMINI_API_KEY
                api_key = GEMINI_API_KEY
            except Exception:
                api_key = None

        if not api_key:
            return (
                "I don't have a strong match for that yet, and my AI fallback "
                "isn't configured (missing Groq API key)."
            )

        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": question}],
        )
        return response.choices[0].message.content

    except Exception as e:  # noqa: BLE001
        print(f"[WARN] Groq fallback failed: {e}")
        return (
            "I don't have a strong match for that yet, and my AI fallback "
            "is unavailable right now. Try rephrasing, or ask about AWS, "
            "DevOps, or sports."
        )


def run_pipeline(user_input: str) -> dict:
    """Mirrors src/predict.py's loop, returns a structured result instead of printing."""

    tokens = preprocess(user_input)
    no_stops = remove_stopwords(tokens)
    lemmas = lemmatize(no_stops)
    processed_text = " ".join(lemmas)

    vectorized = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized)

    intent = label_encoder.inverse_transform(prediction)[0]
    probabilities = model.predict_proba(vectorized)
    confidence = float(max(probabilities[0]))

    pipeline_debug = {
        "tokens": tokens,
        "after_stopwords": no_stops,
        "lemmatized": lemmas,
        "processed_text": processed_text,
        "predicted_intent": intent,
        "confidence": round(confidence, 4),
        "threshold": CONFIDENCE_THRESHOLD,
    }

    if confidence < CONFIDENCE_THRESHOLD:
        ai_response = ask_groq(user_input)
        return {
            "reply": ai_response,
            "source": "llama-3.1-8b-instant (groq)",
            "intent": "unknown",
            "confidence": round(confidence, 4),
            "debug": pipeline_debug,
        }

    reply = get_response(intent)
    return {
        "reply": reply,
        "source": "naive-bayes",
        "intent": intent,
        "confidence": round(confidence, 4),
        "debug": pipeline_debug,
    }


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "ok" if model is not None else "degraded",
            "model_loaded": model is not None,
            "load_error": load_error,
        }
    )


@app.route("/api/chat", methods=["POST"])
def chat():
    if model is None or vectorizer is None or label_encoder is None:
        return (
            jsonify(
                {
                    "error": "Model artifacts not loaded on the server.",
                    "detail": load_error,
                }
            ),
            503,
        )

    data = request.get_json(silent=True) or {}
    user_input = (data.get("message") or "").strip()

    if not user_input:
        return jsonify({"error": "Field 'message' is required and cannot be empty."}), 400

    try:
        result = run_pipeline(user_input)
        return jsonify(result)
    except Exception as e:  # noqa: BLE001
        traceback.print_exc()
        return jsonify({"error": "Internal error processing message.", "detail": str(e)}), 500


@app.route("/api/intents", methods=["GET"])
def intents():
    """Lets the frontend show which intents the model actually knows."""
    try:
        known = list(label_encoder.classes_) if label_encoder is not None else []
    except Exception:
        known = []
    return jsonify({"intents": known})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
