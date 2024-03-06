class MinMaxWordFinder:
    def __init__(self):
        self.text = []

    def add_sentence(self, new):
        for i in new.split():
            self.text.append((len(i), i))

    def shortest_words(self):
        return sorted([j[1] for j in self.text if j[0] == sorted([i[0] for i in self.text])[0]])

    def longest_words(self):
        return sorted(set([j[1] for j in self.text if j[0] == sorted([i[0] for i in self.text])[-1]]))


finder = MinMaxWordFinder()
finder.add_sentence("Hi my dear friend")
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

# print(finder.text)
