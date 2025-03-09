import unittest
from movement_of_pieces.knight import Knight


class TestKnight(unittest.TestCase):
    def setUp(self):
        self.knight = Knight()
        self.opponent_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.pieces = ["n", "b", "q", "k", "r", "p"]

    def test_knight_cannot_move(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", ".", "p", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "r", "b", "n", "r"]]
        row = 8
        col = 1
        legals_in_position = self.knight.knight_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_knight_can_move_anyway(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "n", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", ".", ".", ".", "p", "p"],
            ["r", "n", "b", "q", "k", "b", ".", "p"]]
        row = 5
        col = 4
        legals_in_position = self.knight.knight_movement(
            test_board, row, col, self.pieces)
        self.assertCountEqual([(3, 3), (3, 5), (7, 3), (7, 5),
                              (4, 6), (4, 2), (6, 6), (6, 2)], legals_in_position)

    def test_knight_can_eat_a_piece_anywhere(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "P", ".", "P", ".", "."],
            [".", ".", "P", ".", ".", ".", "P", "."],
            [".", ".", ".", ".", "n", ".", ".", "."],
            [".", ".", "P", ".", ".", ".", "P", "."],
            [".", ".", ".", "P", ".", "P", ".", "."],
            ["r", "n", "b", "q", "k", "b", ".", "p"]]
        row = 5
        col = 4
        legals_in_position = self.knight.knight_movement(
            test_board, row, col, self.pieces)
        self.assertCountEqual([(3, 3), (3, 5), (7, 3), (7, 5),
                              (4, 6), (4, 2), (6, 6), (6, 2)], legals_in_position)
