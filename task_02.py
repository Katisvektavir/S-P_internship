def coincidence(lst=[], interval=[]):
    return [i for i in lst if (isinstance(i, (int, float)))
            and interval.start <= i < interval.stop]
