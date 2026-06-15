from preprocessing import preprocess
from stop_words_removal import remove_stopwords
from lemmatizer import lemmatize

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("KDS: GoodBye!, See you Soon")
        break

    lower_case_text_tokenize = preprocess(user_input)
    rm_stop_words = remove_stopwords(lower_case_text_tokenize)
    lemmitized_words = lemmatize(rm_stop_words)

    print("After Lowering and tokenized : ", lower_case_text_tokenize)
    print("Removed: ", rm_stop_words)
    print("Lemittized words are : ", lemmitized_words)