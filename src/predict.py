import joblib
from response_engine import get_response
from preprocessing import preprocess
from stop_words_removal import remove_stopwords
from lemmatizer import lemmatize
from llama_ai import ask_ask
from logger.chat_logger import ChatLogger




from config import (
    MODEL_FILE,
    TFIDF_FILE,
    LABEL_ENCODER_FILE,
    CONFIDENCE_THRESHOLD,
)

model = joblib.load(MODEL_FILE)

vectorizer = joblib.load(TFIDF_FILE)

label_encoder = joblib.load(LABEL_ENCODER_FILE)

logger = ChatLogger()

while True:

    user_input =input("YOU: ")

    if user_input.lower() == "exit":
        print("GOODBYE! See you Soon :)")
        break

    #NLP PreProcessing
    tokenization_words_final = preprocess(user_input)

    rm_stopped_words_final = remove_stopwords(tokenization_words_final)

    lemmit_words_final = lemmatize(rm_stopped_words_final)

    processed_text = " ".join(lemmit_words_final)

    vectorization_final = vectorizer.transform([processed_text])

    #prediction = model.predict(vectorization_final)


    # Adding confidence score to predict the correct output
    #intent = label_encoder.inverse_transform(prediction)
    #probabilities = model.predict_proba(vectorization_final)
    #confidence = max(probabilities[0])
    probabilities = model.predict_proba(vectorization_final)

    predicted_index = probabilities[0].argmax()

    confidence = probabilities[0][predicted_index]

    intent = label_encoder.inverse_transform([predicted_index])[0]
        

    if confidence < CONFIDENCE_THRESHOLD:
        print("KDS_BOT: Hmm Let me Think........")
        ai_response = ask_ask(user_input)
        print("KDS_BOT: ", ai_response)
       
        logger.log_chat(
            user_input=user_input,
            predicted_intent="unknown",
            confidence=confidence,
            response_source="llm",
            bot_response=ai_response,
        )
        continue

    response = get_response(intent)

    print("KDS_BOT:", response)