import json
from difflib import get_close_matches

dictionary_data = json.load(open("data.json"))

def search_word(word):
    word = word.lower()
    if word in dictionary_data:
        return dictionary_data[word]
    elif word.title() in dictionary_data:
        return dictionary_data[word.title()]
    elif word.upper() in dictionary_data:
        return dictionary_data[word.upper()]
    elif len(get_close_matches(word,dictionary_data.keys(),cutoff=0.8)):
        similar_word = get_close_matches(word,dictionary_data.keys(),cutoff=0.8)
        print("Are you looking %s instead" % similar_word[0])
        search_suggestion = input("Are you looking %s instead? Enter 'Y' if yes or 'N' if no: ")
        if search_suggestion.lower() == "y":
            return dictionary_data[similar_word[0]]
        elif search_suggestion.lower() == "n":
            return "The word doesn't exist. Please double check the word."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check the word."

word = input("Enter a word to search: ")
exp_output = search_word(word)
if type(exp_output) == str:
    print(exp_output)
else:
    for meaning in exp_output:
        print(meaning)
