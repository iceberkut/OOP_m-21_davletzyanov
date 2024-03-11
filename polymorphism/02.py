class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.line = []
        self.lines = []

    def add_word(self, word):
        if len(self.line) + len(word) + 1 <= self.width:
            self.line.append(word)
            self.line.append(' ')
        else:
            self.lines.append(''.join(self.line))
            self.line = [word, ' ']

    def end(self):
        self.lines.append(''.join(self.line))
        self.line = []
        for line in self.lines:
            print(line)
        self.lines = []


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.line = []
        self.lines = []

    def add_word(self, word):
        if len(self.line) + len(word) + 1 <= self.width:
            self.line.insert(0, ' ')
            self.line.insert(0, word)
        else:
            self.lines.append(''.join(self.line))
            self.line = [word, ' ']

    def end(self):
        self.lines.append(''.join(self.line))
        self.line = []
        for line in self.lines:
            print(line.rjust(self.width))
        self.lines = []


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()