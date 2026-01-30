import re

def count_words(string):
    answer = {}
    string = re.split(" |,|\.|\!|\?|-* |:|;|\"", string)
    string = list(map(str.lower, string))
    for i in string:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1
    if "" in answer:
        answer.pop("")
    return answer
