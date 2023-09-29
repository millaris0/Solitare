import deck


class Stack:
    """
    The class models the essence of the pile on the table, which is empty at the beginning,
    into which the cards will be laid out in descending order during the game (King is a starting card).
    """

    def __init__(self):
        self.stack = []
        self.card = deck.Card()
        self.values = {'A': 13, '2': 12, '3': 11, '4': 10, '5': 9, '6': 8, '7': 7, '8': 6, '9': 5, '10': 4, 'J': 3,
                       'Q': 2, 'K': 1}

    def top(self):
        self.card = self.stack[-1]
        return self.card

    def len(self):
        return len(self.stack)

    def full(self):
        return len(self.stack) == len(self.values)

    def can_put(self, card):
        if self.len() == 0:
            if card.get_value == 1:
                return True
            else:
                return False
        else:
            if (self.top().get_value + 1 == card.get_value) and (card.get_suit == self.top().get_suit):
                return True
            else:
                return False

    def put(self, card):
        self.stack.append(card)

    def show_stack(self):
        for card in self.stack:
            print(card.show_card(), end='\t') # прибрала спілкування з користувачем у вигляді print('empty')

    def __iter__(self):
        self.index = 0
        return self

    def __getitem__(self, index):
        return self.stack[index]

    def __next__(self):
        if self.index < self.len():
            c = self.stack[self.index]
            self.index += 1
            return c
        else:
            raise StopIteration


class PlayRow:
    """
    The class models the essence of the row of an eight-card row that is initially laid out from a shuffled deck.
    During the game, this row fills up from bindeck.
    """

    def __init__(self):
        self.row = []

    def base_row(self, d):
        for c in d[0:8]:
            self.row.append(c)
        return self.row

    def get_card(self, index):
        crd = self.row[index]
        self.row[index] = deck.Card("0", "0")
        return crd

    def len(self):
        return len(self.row)

    def put_card(self, index, card):
        self.row[index] = card
        return self.row

    def show_row(self):
        for card in self.row:
            print(card.show_card())

    def __getitem__(self, index):
        return self.row[index]


class BinDeck:
    """
    This class models the stack entity, into which cards from the deck are being flipped for viewing.
    The user can only see the top card.
    """

    def __init__(self):
        self.bin = []

    def put(self, card):
        self.bin.append(card)

    def len(self):
        return len(self.bin)

    def top(self):
        if self.len():
            return self.bin[-1]
        else:
            return "empty"

    def away(self):
        return self.bin.pop()

    def show_bin(self):
        if self.top() == "empty":
            return "empty"
        else:
            return self.top().show_card()
