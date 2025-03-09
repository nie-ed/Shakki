import unittest
from movement_of_pieces.rook import Rook


class TestRook(unittest.TestCase):
    def setUp(self):
        self.rook = Rook()
        self.opponent_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.pieces = ["n", "b", "q", "k", "r", "p"]

    def test_rook_cannot_move(self):
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
        col = 4
        legals_in_position = self.rook.rook_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_rook_can_move_anyway_also_on_opponent_piece(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", ".", ".", ".", "r", ".", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "P", "b", "n", "p"]]
        row = 5
        col = 4
        legals_in_position = self.rook.rook_movement(
            test_board, row, col, self.pieces)
        self.assertCountEqual([(4, 4), (3, 4), (2, 4), (5, 3), (5, 2), (5, 1), (
            5, 0), (5, 5), (5, 6), (5, 7), (6, 4), (7, 4), (8, 4)], legals_in_position)

    def test_rook_cannot_move_past_board(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "p", "r"],
            ["P", "P", "P", "P", "P", "P", "P", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "p"]]
        row = 1
        col = 7
        legals_in_position = self.rook.rook_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_rook_cannot_move_past_up_rigth_board(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "p", "r"],
            ["P", "P", "P", "P", "P", "P", "P", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "p"]]
        row = 1
        col = 7
        legals_in_position = self.rook.rook_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_rook_cannot_move_past_up_left_board(self):
        test_board = [
            [],
            ["r", "p", "B", "Q", "K", "B", "N", "R"],
            ["p", "P", "P", "P", "P", "P", "P", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["p", "n", "b", "q", "k", "b", "n", "p"]]
        row = 1
        col = 0
        legals_in_position = self.rook.rook_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_rook_cannot_move_past_bottom_left_board(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "p"]]
        row = 8
        col = 0
        legals_in_position = self.rook.rook_movement(
            test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)
