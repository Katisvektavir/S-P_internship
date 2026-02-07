class EvenNumbers():
    def __init__(self, even_position=None):
        self.even_position = even_position

    def __iter__(self):
        if isinstance(self.even_position, int):
            for i in range(self.even_position):
                yield i * 2
        else:
            yield None
