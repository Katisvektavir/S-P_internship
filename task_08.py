from functools import reduce

def multiply_numbers(inputs):
    return reduce(lambda x, y: x * y, [int(w) for w in str(inputs) if w.isdigit()])
