from functools import reduce


def multiply_numbers(inputs=None):
    if inputs and any(char.isdigit() for char in str(inputs)):
        return reduce(lambda x, y: x * y, [int(w) for w in str(inputs) if w.isdigit()])
    else:
        return None
