import unittest
from movement_of_pieces.queen import Queen


class TestRook(unittest.TestCase):
    def setUp(self):
        self.queen = Queen()
        self.opponent_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.pieces = ["n", "b", "q", "k", "r", "p"]

    def test_queen_cannot_move(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "r", "b", "n", "k"]]
        row = 8
        col = 3
        legals_in_position = self.queen.queen_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_queen_can_move_anyway_also_on_opponent_piece(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", ".", ".", ".", "q", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "P", "p", ".", "p", "P", "p"],
            ["r", "n", "b", "p", "P", "b", "n", "p"]]
        row = 5
        col = 4
        legals_in_position = self.queen.queen_movement(
            test_board, row, col, self.pieces)
        self.assertCountEqual([(4, 4), (3, 4), (2, 4), (5, 3), (5, 2), (5, 1), (5, 0), (5, 5), (5, 6), (5, 7), (6, 4), (
            7, 4), (8, 4), (6, 3), (6, 5), (4, 3), (3, 2), (2, 1), (4, 5), (3, 6), (2, 7), (7, 6), (7, 2)], legals_in_position)

    def test_queen_cannot_move_past_upper_right_board_corner_or_own_pieces(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "p", "q"],
            ["P", "P", "P", "P", "P", "P", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", ".", "."],
            ["r", "n", "b", ".", "k", "b", "n", "."]]
        row = 1
        col = 7
        legals_in_position = self.queen.queen_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_queen_cannot_move_past_upper_left_board_corner_or_own_pieces(self):
        test_board = [
            [],
            ["q", "p", "B", "Q", "K", "B", "p", "r"],
            ["p", "p", "P", "P", "P", "P", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", "p", "p", "p", "p"],
            [".", "n", "b", ".", "k", "b", "n", "p"]]
        row = 1
        col = 0
        legals_in_position = self.queen.queen_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_queen_cannot_move_past_bottom_left_corner_or_own_pieces(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["r", "p", "p", "p", "p", "p", "p", "p"],
            ["q", "n", "b", ".", "k", "b", "n", "p"]]
        row = 8
        col = 0
        legals_in_position = self.queen.queen_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_queen_cannot_move_past_bottom_right_corner_or_own_pieces(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "q"]]
        row = 8
        col = 7
        legals_in_position = self.queen.queen_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)
