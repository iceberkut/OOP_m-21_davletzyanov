class Selector:
    def __init__(self, values):
        self.odd_nums = list()
        self.even_nums = list()
        for i in values:
            if i % 2 != 0:
                self.odd_nums.append(i)
            else:
                self.even_nums.append(i)

    def get_odds(self):
        return self.odd_nums

    def get_evens(self):
        return self.even_nums


values = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
