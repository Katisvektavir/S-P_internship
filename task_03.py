def max_odd(array):
    current_max = 0
    for i in array:
        if (isinstance(i, (int, float))
                and i % 1 == 0
                and i % 2 != 0
                and current_max < i):
            current_max = i
    return current_max if current_max != 0 else None
