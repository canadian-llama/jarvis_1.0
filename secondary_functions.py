import nltk


def input_tokenizer(query: str):
    return nltk.word_tokenize(query)


def input_comparison(tokenized_input: list, word_list: list):
    input_set = set(tokenized_input)
    word_list_set = set(word_list)

    common_words = bool(input_set & word_list_set)
    return common_words


def word_list_tokenizer(word_list: list):
    words = ""
    for word in word_list:
        words = word.lower()
    tokenized_word_list = input_tokenizer(words)
    return tokenized_word_list
