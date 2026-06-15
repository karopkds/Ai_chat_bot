import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def remove_stopwords(lower_case_text_tokenize):
    stopswords = set(stopwords.words('english'))

    if len(lower_case_text_tokenize) <=2:
        return lower_case_text_tokenize

    removed_stops_words = [i for i in lower_case_text_tokenize if i not in stopswords]

    return removed_stops_words




