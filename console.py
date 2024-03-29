from play import Game


class Console(Game):

    def __init__(self):
        super().__init__()
        self.play()

    def get_play_field(self):
        playdeck_card = None
        playbin_card = None
        if self._playdeck:
            playdeck_card = self._playdeck.top()
        if self._playbin:
            playbin_card = self._playbin.top()

        base_cards = []
        if self._base:
            for stack in self._base:
                base_cards.append(stack.top())
        else:
            for i in range(self.NBASE):
                base_cards.append(None)
        base_card_message = ""
        for i in range(self.NBASE):
            base_card_message += f"| {i+ 1}. {base_cards[i]} "

        play_columns_message = ""
        for i in range(self.NPLAY_ROWS):
            play_columns_message += f"    Row {i + 1} "
            for n in range(self.NPLAY):
                play_columns_message += f"| {n + 1}. {self._play[i][n]} "

            play_columns_message += "\n"

        play_field = f"---- PLAY FIELD ----\n" \
                     f"PlayDeck: |{playdeck_card}|\n" \
                     f"PlayBin: |{playbin_card}|\n" \
                     f"Base Row: {base_card_message} |\n" \
                     f"Play Rows:\n{play_columns_message}\n" \
                     f"*****************\n\n"
        return play_field

    def move_cards(self):

        try:
            var = int(input("Choose number of operation for card movement from/to:\n"
                            "1: deck/play row\n"
                            "2: deck/bin\n"
                            "3: deck/base row\n"
                            "4: bin/play row\n"
                            "5: bin/base row\n"
                            "6: play row/ play row\n"
                            "7: play row/ base row\n"
                            ))

            result = True
            if var == 1:
                row = int(input("Write coordinates to which row you want move your card: "))
                col = int(input("Write coordinates to column you want move your card: "))
                result = self.deck_play(row - 1, col - 1)

            if var == 2:
                result = self.deck_bin()

            if var == 3:
                col = int(input("Write to which column you want move your card: "))
                result = self.deck_base(col - 1)

            if var == 4:
                row = int(input("Write to which row you want move your card: "))
                col = int(input("Write to which column you want move your card: "))
                result = self.bin_play(row - 1, col - 1)

            if var == 5:
                col = int(input("Write to column you want move your card: "))
                result = self.bin_base(col - 1)

            if var == 6:
                row_fr = int(input("Write coordinates from which row you want move your card: "))
                col_fr = int(input("Write coordinates from which column you want move your card: "))
                row_to = int(input("Write coordinates to which row you want move your card: "))
                col_to = int(input("Write coordinates to which column you want move your card: "))
                result = self.play_play(row_fr - 1, col_fr - 1, row_to - 1, col_to - 1)

            if var == 7:
                row_fr = int(input("Write coordinates from which row you want move your card: "))
                col_fr = int(input("Write coordinates from which column you want move your card: "))
                col_to = int(input("Write coordinates to which column you want move your card: "))
                result = self.play_base(row_fr - 1, col_fr - 1, col_to - 1)

            elif var not in range(1, 8):
                print(f"There is no operation: {var}\n"
                      f"Chose another one from the list;)")

        except ValueError:
            print('Enter the coordinates of the position you want your card to move to,\n'
                  'using a numerical value for the destination.')
        except IndexError:
            print(f"IndexError: Index is out of range.")
        if not result:
            print("Please, check that:\n"
                  "- you chose the appropriate position for card move\n"
                  "- you put your card in an appropriate position and \n "
                  "- the logic of card's sequence monotonically increase still work\n"
                  )

    def play(self):
        print("Мета пасьянсу: необхідно зібрати всі карти на базових стопках у висхідних послідовностях у масть.\n\n"
            "Правила пасьянсу. З колоди виймаються тузи й кладуться в один ряд. Це базові карти, на яких\n"
            "необхідно вибудувати висхідні послідовності в масть. Колода ретельно тасується й під базовими картами\n"
            "викладається 2 горизонтальних ряди по 6 карт. Це ігрові карти. Колоду, що залишилася, кладемо ліворуч,\n"
            "під колодою знаходиться допоміжна комірка. Карти з ігрових місць і з колоди дозволяється переміщати\n"
            "в базові стопки у висхідній послідовності в масть. Якщо ігрова карта переміщена й звільняється місце, то\n"
            "необхідно покласти карту з колоди. Колода проглядається один раз.\n\n")
        while self._in_play:
            print(self.get_play_field())
            self.move_cards()
            self.win()
