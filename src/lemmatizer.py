import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


def get_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_map = {'J': wordnet.ADJ, 'V': wordnet.VERB, 'N': wordnet.NOUN, 'R': wordnet.ADV}
    return tag_map.get(tag, wordnet.NOUN)

def lemmatize(lower_case_text_tokenize):
    lemmit = WordNetLemmatizer()

    lemitized = [lemmit.lemmatize(i, get_pos(i)) for i in lower_case_text_tokenize]

    return lemitized


