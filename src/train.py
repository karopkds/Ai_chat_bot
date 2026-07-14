import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.calibration import CalibratedClassifierCV 
from preprocessing import preprocess
from stop_words_removal import remove_stopwords
from lemmatizer import lemmatize
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


df = pd.read_csv("data/intents.csv")
# Assigning X and Y access
processed_sentences = []


for sentence in df["sentence"]:

    tokens = preprocess(sentence)

    filtered = remove_stopwords(tokens)

    lemmatized = lemmatize(filtered)

    processed_text = " ".join(lemmatized)

    processed_sentences.append(processed_text)

X = processed_sentences


Y = df["intent"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify= Y
)

# Now i'm converting into vector formate so ML can understand
vectorizing_Traning = TfidfVectorizer()
X_train_tfidf = vectorizing_Traning.fit_transform(X_train)
X_test_tfidf = vectorizing_Traning.transform(X_test)


#print(X_tfidf)

# Convert labels into numbers
label_encoder = LabelEncoder()
Y_train_encoded = label_encoder.fit_transform(Y_train)
Y_test_encoded = label_encoder.transform(Y_test)
print(Y_train_encoded)

# Now the Actual Trainig Begins
# We are using Navie Byes MultinimialNB (Best for Spam Detection, Sentimental Analysis, Email Categorization)

model = MultinomialNB()
model = CalibratedClassifierCV(model, cv=3, method='isotonic')
model.fit(X_train_tfidf, Y_train_encoded)
Y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(Y_test_encoded, Y_pred)
print(f"Model Accuracy: {accuracy:.2%}")
print("\nClassification Report:\n")

print(
    classification_report(
        Y_test_encoded,
        Y_pred,
        target_names=label_encoder.classes_,
        zero_division=0
    )
)
cm = confusion_matrix(Y_test_encoded, Y_pred)

plt.figure(figsize=(8, 6))

plt.imshow(cm)

plt.title("Confusion Matrix")

plt.colorbar()

plt.xticks(
    range(len(label_encoder.classes_)),
    label_encoder.classes_,
    rotation=45,
)

plt.yticks(
    range(len(label_encoder.classes_)),
    label_encoder.classes_,
)

plt.xlabel("Predicted Label")

plt.ylabel("True Label")

plt.tight_layout()

plt.show()

# NOW WE ARE SAVING THE MODEL Traing data. So we are using joblib Libarrary
# So we dont want to train again and again when we retstart the VSCODE

joblib.dump(model, "models/model.pkl")

joblib.dump(vectorizing_Traning, "models/tfidf.pkl")

joblib.dump(label_encoder, "models/label_encoder.pkl")

print("\nTraining Completed Successfully")