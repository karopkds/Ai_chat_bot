import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    return tokens