import re

def count_words(sentence):

    dictionary = {}

    #return all non-verlapping matches of a pattern in a string as a list of strings
    sentence = re.findall(r"[a-z]+'?[a-z]+|[a-z]+|\d+", sentence.lower())

    for word in sentence:
        dictionary[word] = sentence.count(word)
    
    return dictionary
    