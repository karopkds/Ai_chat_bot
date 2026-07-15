import joblib
from response_engine import get_response
from preprocessing import preprocess
from stop_words_removal import remove_stopwords
from lemmatizer import lemmatize
from llama_ai import ask_ask
from logger.chat_logger import ChatLogger
from conversation_memory import ConversationMemory
from decision_engine import is_contextual_followup
from chat_response import build_response





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
memory = ConversationMemory() #This creates one memory object for the current chatbot session.

def process_message(user_input):

    is_follow_up = is_contextual_followup(
        user_input=user_input,
        memory=memory
    )

    if is_follow_up:

        prompt = f"""
    The user is continuing an existing conversation.

    Topic:
    {memory.last_intent}

    Original Question:
    {memory.last_user_message}

    Previous Answer:
    {memory.last_bot_response}

    The user now asks:

    {user_input}

    Continue the explanation naturally.
    Do not repeat the previous answer.
    Give more detail and practical examples.
    """
        reply = ask_ask(prompt)
        source = "follow_up"

        memory.update(
            intent=memory.last_intent,
            user_message=user_input,
            bot_response=reply,
        )

        logger.log_chat(
            user_input=user_input,
            predicted_intent=memory.last_intent,
            confidence=1.0,
            response_source=source,
            bot_response=reply,
        )

        return {
            "reply": reply,
            "intent": memory.last_intent,
            "confidence": 1.0,
            "source": source,
            "success": True,
        }

    tokenization_words_final = preprocess(user_input)

    rm_stopped_words_final = remove_stopwords(tokenization_words_final)

    lemmit_words_final = lemmatize(rm_stopped_words_final)

    processed_text = " ".join(lemmit_words_final)

    vectorization_final = vectorizer.transform([processed_text])
    probabilities = model.predict_proba(vectorization_final)

    predicted_index = probabilities[0].argmax()
    confidence = probabilities[0][predicted_index]

    intent = label_encoder.inverse_transform([predicted_index])[0]


    if confidence < CONFIDENCE_THRESHOLD:
        print("KDS_BOT: Hmm Let me Think........")
        reply = ask_ask(user_input)
        print("KDS_BOT: ", reply)
        source = "llm"
        
        memory.update(
            intent="unknown",
            user_message=user_input,
            bot_response= reply
        )
    else :

        reply = get_response(intent)

        source = "machine_learning"

        memory.update(
            intent=intent,
            user_message=user_input,
            bot_response=reply,
        )
       
    logger.log_chat(
            user_input=user_input,
            predicted_intent=intent,
            confidence=confidence,
            response_source=source,
            bot_response=reply,
    )

    return build_response(
    reply=reply,
    intent=intent,
    confidence=confidence,
    source=source,
)

if __name__ == "__main__":

    while True:

        user_input = input("YOU: ")

        if user_input.lower() == "exit":
            break

        result = process_message(user_input)

        print(result)