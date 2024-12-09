import unittest

from board import Board
from game import Game


class Test(unittest.TestCase):
    def setUp(self):
        self.user_board = Board()
        user_board_representation = Board()
        self.computer_board = Board()
        computer_board_representation = Board()
        self._game = Game(self.user_board, self.computer_board, user_board_representation, computer_board_representation)


    def test(self):
        # useer_board = Board()
        # computer_board = Board()
        self.assertEqual(self._game.place_computer_ship(self.computer_board), True)
        self.assertEqual(self._game.is_win(), False)
        self.assertEqual(self._game.player_shot(1, 1, self.computer_board), 'miss')
        self.assertEqual(self._game.computer_move(), 'miss')
        self.assertEqual(self._game.place_player_ship(self.user_board), True)