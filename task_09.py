def sum_key(dictionary):
    return sum(dictionary.values())

def drop_keys_less_ten(dictionary):
    bigger_keys = [key for key, value in dictionary.items() if value < 10]
    for key in bigger_keys:
        dictionary.pop(key)

def sorted_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))


def connect_dicts(dict1, dict2):
    bigger, smaller = (dict1.copy(), dict2.copy()) if sum_key(dict1) > sum_key(dict2) else (dict2.copy(), dict1.copy())
    drop_keys_less_ten(bigger)
    drop_keys_less_ten(smaller)
    for key, value in smaller.items():
        if key not in bigger:
            bigger[key] = value

    return sorted_dict_by_value(bigger)
