"""
The author of this program is Myroslava Tsvietkova, K-13 group.

                                 ||Rules of a solitaire||
Number of decks: 2
Number of cards in one deck: 52

The goal of solitaire is to collect all the cards on the base stacks in descending sequences in a suit.

Two decks are mixed into one. The resulting deck is carefully shuffled and
8 game stacks are laid out, one card in each stack. The remaining log is placed next to it.
On top is a row of eight base piles of starting cards that have kings laying
there during the game. The cards of the game piles are allowed to be used for conversion into the base piles
in ascending sequences in suits. Empty playing stacks are filled with cards from a deck that
remained It is allowed to view the cards of the deck. The deck is not transferable.
Solitaire is won if all the cards are collected on the base piles in ascending sequences in the suit.
"""
import deck
import play
import game


BREAK_STRING = "=============================================="


def valid_commands():
    print("Valid commands:")

    commands = {"help": "- help", "quit": "- stop the game", "from deck to bin": "- turn over top card from deck",
                "move to stack 1-8": "- move card to stack with chosen index",
                "move to row 1-8": "- move card to chosen place in the row",
                "get card from row 1-8": "- you can take card from the exact place in row",
                "get card from bin": "- you can take card from bin"
                }
    for key, value in commands.items():
        print(f'{key} {value}')
    print("\n" + BREAK_STRING)


def table(s, r, b):
    print("\n" + BREAK_STRING)
    print(f"Bin\t{b.show_bin()}")
    print("Row")
    r.show_row()
    print("\nStacks")
    for stack in s:
        if stack.len() == 0:
            print('empty')   # змінила вивід
        else:
            stack.show_stack()
            print()


def entry():
    """
    This is a game login function. Here the player's commands are transmitted,
    the interface is displayed, and errors that may occur during the game are handled.
    :return: result of the move
    """
    s = [play.Stack() for _ in range(8)]
    d = deck.Deck()
    b = play.BinDeck()
    r = play.PlayRow()

    try:
        print("\n" + BREAK_STRING)
        print("Welcome to Solitaire 'Horizon'!")
        print(__doc__)
        g = game.Game(d, r, b, s)
        r = g.new_game()
        table(s, r, b)

        game_over = False

        while not game_over:
            command = input("Enter a command (type 'help' to see valid commands):")
            if command == "help":
                valid_commands()
            elif command == "quit":
                raise KeyboardInterrupt("You've stopped the game")
            else:
                move_made = g.move(command)
                table(s, r, b)
                if move_made is False:
                    print('Oops, your move was wrong, try again')
                if g.win():
                    game_over = True
                    print("Congratulations! You've won!")

    except KeyboardInterrupt:
        print("You've stopped the game")


entry()

