from difflib import SequenceMatcher
import csv

def getInputs(fileName):
    fields = []
    # Assuming the first row of data represent the columns
    with open(fileName, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if(len(row) != 0):
                fields = row
                break
    return fields


def initialize_dictionary():
    """Dictionary matches the string field to an array of boolean value compliance guidelines as follows: inputField: [encryption, masking]"""

    identified_PIIs = {
        "Name": [True, False],
        "Age": [True, False], 
        "Date of Birth": [True, False],
        "Credit Card": [False, True],
        "Phone #": [True, True],
        "Address": [True, False],
        "Email": [True, True],
        "Credit Score": [True, True],
        "Device ID": [True, True]
    } 
    return identified_PIIs

# Uses Levenshtein distance to determine the similarity between two strings and returns a ratio between 0 and 1
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def acronym(string):
    return ''.join(string[0].upper() for string in string.split())


def getValue(key, identified_PIIs):
    return identified_PIIs.get(key)


# This function matches the input value in the .csv file (keyValue) to a key in the identified_PIIs dictionary. It takes into account
# capitalization and minor typos, as well as acronyms and some cases of similar meanings.
def matcher(keyValue, identified_PIIs):
    # these variables are initialized so that they can be used in case there are typos (and words don't directly match).
    # this case will be handled at the end of the outer for loop.
    greatestSimilarity = 0 # represents the greatest similarity score between a key in the dictionary and keyValue
    bestMatch = None

    # loops through all of the keys in the dictionary
    for key in identified_PIIs: 
        curSimilarity = similarity(key.casefold(), keyValue.casefold()) 

        if(curSimilarity >= 0.8): # if keyValue is 100% similar to the key, just return the key
            return key
        elif (curSimilarity <= 0.2): # if the keyValue is not even close to the key, skip to the next key
            continue
        
        # Marks the start where the function deals with similar names
        keyValueList = keyValue.split(' ') 
        firstWordKeyValue = keyValueList[0].casefold() # first word in keyValue
        firstWordKey = key.split(' ', 1)[0].casefold() # "" in key
        count = 0 

        # counts how many of the words in keyValue are in key
        for word in keyValueList: 
            if word.casefold() in key.casefold():
                count += 1

        # if matches to key reach a certain threshold, or if the similarity is 50% or greater and the first words of key and keyValue match/are similar
        if (count >= 0.6 * (len(keyValueList)) or (curSimilarity >= 0.5 and similarity(firstWordKeyValue,firstWordKey) >= 0.75)):
            bestMatch =  key
        # or if either the key or the keyValue input are acronyms of one another, case-insensitive
        elif (acronym(keyValue).casefold() == key.casefold() or acronym(key).casefold() == keyValue.casefold()): 
            return key
        # last case is setting greatestSimilarity if you only have a near-match
        elif (curSimilarity > greatestSimilarity):
            greatestSimilarity = curSimilarity
            bestMatch = key
    return bestMatch



