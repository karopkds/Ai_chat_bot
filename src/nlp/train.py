import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
import joblib

df = pd.read_csv("data/intents.csv")
# Assigning X and Y access

X = df["sentence"]
Y = df["intent"]

# Now i'm converting into vector formate so ML can understand
vectorizing_Traning = TfidfVectorizer()
X_tfidf = vectorizing_Traning.fit_transform(X)
#print(X_tfidf)

# Convert labels into numbers
label_encoder = LabelEncoder()
Y_encoded = label_encoder.fit_transform(Y)
print(Y_encoded)

# Now the Actual Trainig Begins
# We are using Navie Byes MultinimialNB (Best for Spam Detection, Sentimental Analysis, Email Categorization)

model = MultinomialNB()
model.fit(X_tfidf, Y_encoded)

# NOW WE ARE SAVING THE MODEL Traing data. So we are using joblib Libarrary
# So we dont want to train again and again when we retstart the VSCODE

joblib.dump(model, "models/model.pkl")

print("\nTraining Completed Successfully")