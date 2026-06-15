from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def fit_vectorizer(documents):

    tfidf_matrix = vectorizer.fit_transform(documents)

    return tfidf_matrix

def transform_text(text):

    return vectorizer.transform([text])

def get_features():

    return vectorizer.get_feature_names_out()