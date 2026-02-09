import re


def key_in_dict(dictionary, key):
    if key == '':
        return
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def count_words(text):
    result = {}
    text = re.split(" |,|\.|\!|\?|-* |:|;|\"", text)
    text = list(map(str.lower, text))
    for key in text:
        key_in_dict(result, key)
    return result
