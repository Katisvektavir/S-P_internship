def coincidence(list=[], range=[]):
    return [i for i in list if (isinstance(i, (int, float)))
            and (i > range.start)
            and (i < range.stop)]
