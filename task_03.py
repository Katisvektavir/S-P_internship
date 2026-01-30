def max_odd(array):
    now_max = 0
    for i in array:
        if (isinstance(i, (int, float))
                and i % 1 == 0
                and i % 2 != 0
                and now_max < i):
            now_max = i
    return now_max if now_max != 0 else None
