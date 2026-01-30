def sort_list(list):
    if not list:
        return
    M = max(list)
    m = min(list)
    for i in range(len(list)):
        if list[i] == M:
            list[i] = m
        elif list[i] == m:
            list[i] = M
    list.append(m)
