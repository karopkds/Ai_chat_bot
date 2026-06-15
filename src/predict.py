import joblib
from response_engine import get_response
from preprocessing import preprocess
from stop_words_removal import remove_stopwords
from lemmatizer import lemmatize
from llama_ai import ask_ask


model = joblib.load("models/model.pkl")

vectorizer = joblib.load("models/tfidf.pkl")

label_encoder = joblib.load("models/label_encoder.pkl")

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

    prediction = model.predict(vectorization_final)


    # Adding confidence score to predict the correct output
    intent = label_encoder.inverse_transform(prediction)
    probabilities = model.predict_proba(vectorization_final)
    confidence = max(probabilities[0])
       

    if confidence < 0.60:
        print("KDS_BOT: Hmm Let me Think........")
        ai_response = ask_ask(user_input)
        print("KDS_BOT: ", ai_response)
        continue

    


    response = get_response(intent[0])
   
    print("KDS_BOT: ", response)