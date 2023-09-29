import random


class Card:

    def __init__(self, suit=None, rank=None):
        self.S = ["S", "H", "D", "C"]
        self.R = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
        self.V = {'K': 1, 'Q': 2, 'J': 3, '10': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10,
                  '3': 11, '2': 12, 'A': 13}
        self.suit = suit
        self.rank = rank

    @property
    def get_rank(self):
        return self.rank

    @property
    def get_suit(self):
        return self.suit

    @property
    def get_value(self):
        return self.V.get(self.rank)

    def show_card(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = []
        self.suits = ["S", "H", "D", "C"]
        self.ranks = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
        self.build()

    def build(self):
        self.deck = []
        for _ in range(2):
            for s in self.suits:
                for r in self.ranks:
                    self.deck.append(Card(s, r))

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def draw_card(self):
        if len(self.deck) > 0:
            crd = self.deck.pop()
            return crd
        else:
            return False

    def show_deck(self):
        for c in self.deck:
            print(c.show_card())

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.deck):
            c = self.draw_card()
            self.index += 1
            return c
        else:
            raise StopIteration

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.deck[index]
        elif isinstance(index, slice):
            return self.deck[index.start:index.stop:index.step]


