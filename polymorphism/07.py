class Table:
    def __init__(self, rows, cols):
        self.data = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            return self.data[row][col]
        return None

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def n_rows(self):
        return len(self.data)

    def n_cols(self):
        return len(self.data[0])

    def delete_row(self, row):
        del self.data[row]

    def delete_col(self, col):
        for row in self.data:
            del row[col]

    def add_row(self, row):
        self.data.insert(row, [0] * self.n_cols())

    def add_col(self, col):
        for row in self.data:
            row.insert(col, 0)




tab = Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_col(1)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()