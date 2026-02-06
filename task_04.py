def sort_list(int_list):
    if not int_list:
        return []
    M = max(int_list)
    m = min(int_list)
    result = [M if i == m else m if i == M else i for i in int_list]
    result.append(m)
    return result
