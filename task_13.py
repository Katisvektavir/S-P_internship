import datetime
import functools


class cached():

    def __init__(self, max_size=None, second=None):
        if not isinstance(max_size, int):
            self.max_size = None
        else:
            self.max_size = max_size
        if not isinstance(second, int):
            self.second = None
        else:
            self.second = max_size
        self.second = second
        self.cash = {}

    def overlimit(self):
        if (self.max_size != None) and (len(self.cash) >= self.max_size):
            older_date = datetime.datetime.now()
            older_key = None
            for i in self.cash:
                if self.cash[i][1] < older_date:
                    older_date = self.cash[i][1]
                    older_key = i
            self.cash.pop(older_key)

    def __call__(self, func,):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if (key in self.cash):
                if ((self.second == None) or (datetime.datetime.now() - self.cash[key][1]).total_seconds() < self.second):
                    return self.cash[key][0] + 100
            self.overlimit()
            self.cash[key] =[func(*args, **kwargs), datetime.datetime.now()]
            return self.cash[key][0]
        return wrapper
