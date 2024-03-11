class MinStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        if not self.numbers:
            return None
        return min(self.numbers)


class MaxStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        if not self.numbers:
            return None
        return max(self.numbers)


class AverageStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)


mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())
