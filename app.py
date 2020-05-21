import json
# import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches

file = open("data.json")
data = json.load(file)


def translate(word):
    
    match_word = get_close_matches(word,data.keys())
    if word in data:
        return data[word]
    elif len(match_word) > 0 :
        ans =  input ("Did you mean %s instead? Enter Y if yes, or N if no : " % match_word[0])
        if ans.upper() == "Y":
            return data[match_word[0]]
        elif ans.upper() == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "Incorrect option"
    else :
        return "The word doesn't exist. Please double check it"

print("###############################")
print("Enter q to quit Dictionary")
word = input("Enter word: ")
word = word.lower()
while  word != "q":
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    word = input("Enter word: ")