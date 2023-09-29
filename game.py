import deck


class Game:
    """
    The class for modeling game logic, its methods ensure that actions are performed by the player.
    """

    def __init__(self, tdeck, trow, tbin, tstack):
        self.tdeck = tdeck
        self.tbaserow = trow
        self.tbin = tbin
        self.tstack = tstack
        self.card = deck.Card()

    def new_game(self):
        self.tdeck.build()
        self.tdeck.shuffle()
        self.tbaserow.base_row(self.tdeck)
        return self.tbaserow

    def win(self):
        k = 0
        for i in range(0, len(self.tstack)):
            if self.tstack[i].full():
                k += 1
        if k == 8:
            return True
        else:
            return False

    def move(self, command):
        if command == "from deck to bin":
            return self.tbin.put(self.tdeck.draw_card())

        elif "move to stack" in command:
            num = int(command[-1])
            if num > 8 or num < 1:
                return False
            elif self.tstack[num - 1].can_put(self.card):
                return self.tstack[num - 1].put(self.card)

        elif "move to row" in command:
            num = int(command[-1])
            if num > 8 or num < 1:
                return False
            elif self.tbaserow[num - 1].get_suit == "0" and \
                    self.tbaserow[num - 1].get_rank == "0":
                return self.tbaserow.put_card(num - 1, self.card)

        elif "get card from row" in command:
            num = int(command[-1])
            if num > 8 or num < 1:
                return False
            elif self.tbaserow[num - 1].get_suit != 0 and \
                    self.tbaserow[num - 1].get_rank != 0:
                self.card = self.tbaserow.get_card(num - 1)
                return self.card

        elif command == "get card from bin":
            if self.tbin.top() != "empty":
                self.card = self.tbin.away()
                return self.card
            else:
                return False
