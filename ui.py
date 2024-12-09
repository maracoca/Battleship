from board import Board
from game import Game


class UI:
    def __init__(self, game):
        self._game = game

    def start(self):

        start = 's'

        user_input = input('Type s to start the game. ').lower()
        while user_input not in start:
            print('Wrong input')
            user_input = input('Type s to start the game. ').lower()

        try:
            if user_input == start:
                self._game.start()

            else:
                print('Wrong input')

        except Exception as exception:
            print(exception)


computer_board_representation = Board()
user_board_representation = Board()
user_board = Board()
computer_board = Board()
game = Game(user_board, computer_board, user_board_representation, computer_board_representation)
ui = UI(game)
ui.start()
