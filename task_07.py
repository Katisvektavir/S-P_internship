def combine_anagrams(words_array):
    combine = {}
    for word in words_array:
        split_word = "".join(sorted(word))
        if split_word in combine:
            combine[split_word].append(word)
        else:
            combine[split_word] = []
            combine[split_word].append(word)
    print(combine)
    return [i for i in combine.values()]

