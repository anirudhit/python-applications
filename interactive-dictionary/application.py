import json
from difflib import get_close_matches

dictionary_data = json.load(open("data.json"))

def search_word(word):
    word = word.lower()
    if word in dictionary_data:
        for meaning in dictionary_data[word]:
            print(meaning)
    else:
        similar_word = get_close_matches(word,dictionary_data.keys())
        if len(similar_word):
            print("Are you looking for the similar word " + "\""+ similar_word[0] + "\"")
            search = input("To search type Yes or No to exit: ")
            if search.lower() == "yes":
                search_word(similar_word[0])
        else:
            print("The word is not available. Please check the word")

word = input("Enter a word to search: ")
search_word(word)
