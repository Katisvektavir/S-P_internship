def combine_anagrams(words_array):
    combine = {}
    for word in words_array:
        sorted_word = "".join(sorted(word))
        if sorted_word in combine:
            combine[sorted_word].append(word)
        else:
            combine[sorted_word] = []
            combine[sorted_word].append(word)
    return [i for i in combine.values()]

