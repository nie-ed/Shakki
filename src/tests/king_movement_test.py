import unittest
from movement_of_pieces.king import King

class TestKing(unittest.TestCase):
    def setUp(self):
        self.king = King()
        self.pieces = ["n", "b", "q", "k", "r", "p"]

    def test_king_cannot_move(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 8
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_king_can_move_anyway(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", ".", "b", "n", "r"]]
        row = 5
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, self.pieces)
        self.assertEqual([(4, 4), (6, 4), (5, 3), (5, 5), (4, 3), (4, 5), (6, 3), (6, 5)], legals_in_position)

    def test_king_can_move_down(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", "p", "p", ".", "."],
            ["p", "p", ".", "p", "k", "p", ".", "p"],
            ["r", "n", "b", "q", ".", "b", "n", "r"]]
        row = 7
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, self.pieces)
        self.assertEqual([(8, 4)], legals_in_position)

    def test_king_can_move_up_and_diagonally_up(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 7
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, self.pieces)
        self.assertEqual([(6, 4), (6, 3), (6, 5)], legals_in_position)