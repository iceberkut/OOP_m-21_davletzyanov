class Balance:
    def __init__(self):
        self.weight = 0

    def add_left(self, num):
        self.weight -= num

    def add_right(self, num):
        self.weight += num

    def result(self):
        if self.weight > 0:
            return "R"
        elif self.weight < 0:
            return "L"
        else:
            return "="


balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())
