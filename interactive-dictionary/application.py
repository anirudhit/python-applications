import json
from difflib import SequenceMatcher
dictionary_data = json.load(open("data.json"))

def search_word(word):
    word = word.lower()
    if word in dictionary_data:
        for meaning in dictionary_data[word]:
            print(meaning)
    else:
        similar_word = word_similarity(word)
        if len(similar_word):
            print("Are you looking for the similar word " + "\""+ similar_word + "\"")
            search = input("To search type Yes or No to exit: ")
            if search.lower() == "yes":
                search_word(similar_word)
        else:
            print("The word is not available. Please check the word")

def word_similarity(word):
    word = word.lower()
    similar_word = ""
    for key_word in dictionary_data:
        match_ratio = SequenceMatcher(None, word, key_word).ratio()
        if(match_ratio > 0.8):
            similar_word = key_word
    return similar_word

word = input("Enter a word to search: ")
search_word(word)
