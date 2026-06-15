import joblib
from response_engine import get_response

model = joblib.load("models/model.pkl")

vectorizer = joblib.load("models/tfidf.pkl")

label_encoder = joblib.load("models/label_encoder.pkl")

while True:

    user_input =input("YOU: ")

    if user_input.lower() == "exit":
        print("GOODBYE! See you Soon :)")
        break
    user_vector = vectorizer.transform([user_input])

    prediction = model.predict(user_vector)

    intent = label_encoder.inverse_transform(prediction)


    response = get_response(intent[0])
    
    print("KDS_BOT: ", response)