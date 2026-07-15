import os
import sys
import traceback

from flask import Flask, request, jsonify, send_from_directory
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

from chat_engine import process_message

CONFIDENCE_THRESHOLD = 0.60
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------
# Load model artifacts once at startup
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Groq fallback — isolated import so a missing/blank API key never crashes
# the known-intent path.
# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/api/health")
def health():

    return jsonify(
        {
            "status": "ok",
            "chat_engine": "loaded"
        }
    )


@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    user_input = (data.get("message") or "").strip()
    EXIT_COMMANDS = {
        "exit",
        "quit",
        "bye",
        "goodbye",
    }
    if user_input.lower() == EXIT_COMMANDS:

        return jsonify(
            {
                "reply": "Goodbye! See you soon 👋",
                "intent": "exit",
                "confidence": 1.0,
                "source": "system",
                "success": True,
                "exit": True
            }
        )

    if not user_input:
        return jsonify(
            {
                "error": "Message cannot be empty."
            }
        ), 400

    try:

        result = process_message(user_input)

        return jsonify(result)

    except Exception as e:

        traceback.print_exc()

        return jsonify(
            {
                "success": False,
                "error": str(e)
            }
        ), 500


@app.route("/api/intents", methods=["GET"])
def intents():
    """Lets the frontend show which intents the model actually knows."""
    try:
        known = list(label_encoder.classes_) if label_encoder is not None else []
    except Exception:
        known = []
    return jsonify({"intents": known})


@app.route("/")
def home():
    return send_from_directory(os.path.join(PROJECT_ROOT, "src"), "index.html")


@app.route("/api")
def api_info():
    return jsonify({
        "message": "AI Chatbot API",
        "version": "1.0",
        "health": "/api/health",
        "chat": "/api/chat",
        "intents": "/api/intents"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)