import nltk
from nltk.tokenize import word_tokenize

def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    return tokens