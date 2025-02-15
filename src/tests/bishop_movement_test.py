import unittest
from movement_of_pieces.bishop import Bishop

class TestRook(unittest.TestCase):
    def setUp(self):
        self.bishop = Bishop()
        self.opponent_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.pieces = ["n", "b", "q", "k", "r", "p"]

    def test_bishop_cannot_move(self):
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
        col = 2
        legals_in_position = self.bishop.bishop_movement(test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_bishop_can_move_anyway_also_on_opponent_piece(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "P", "p", "p", "p", "P", "p"],
            ["r", "n", "b", "p", "P", ".", "n", "p"]]
        row = 5
        col = 4
        legals_in_position = self.bishop.bishop_movement(test_board, row, col, self.pieces)
        self.assertCountEqual([(6, 3), (7, 2), (6, 5), (7, 6), (4, 3), (3, 2), (2, 1), (4, 5), (3, 6), (2, 7)], legals_in_position)


    def test_bishop_cannot_move_past_upper_right_board_corner_or_own_pieces(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "p", "b"],
            ["P", "P", "P", "P", "P", "P", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", ".", "."],
            ["r", "n", ".", "q", "k", "b", "n", "."]]
        row = 1
        col = 7
        legals_in_position = self.bishop.bishop_movement(test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)


    def test_bishop_cannot_move_past_upper_left_board_corner_or_own_pieces(self):
        test_board = [
            [],
            ["b", "p", "B", "Q", "K", "B", "p", "r"],
            ["p", "p", "P", "P", "P", "P", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", "p", "p", "p", "p"],
            [".", "n", "p", ".", "k", "b", "n", "p"]]
        row = 1
        col = 0
        legals_in_position = self.bishop.bishop_movement(test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_bishop_cannot_move_past_bottom_left_corner_or_own_pieces(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["r", "p", "p", "p", "p", "p", "p", "p"],
            ["b", "n", "b", ".", "k", "b", "n", "p"]]
        row = 8
        col = 0
        legals_in_position = self.bishop.bishop_movement(test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)

    def test_bishop_cannot_move_past_bottom_right_corner_or_own_pieces(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", ".", "q", "k", "b", "n", "b"]]
        row = 8
        col = 7
        legals_in_position = self.bishop.bishop_movement(test_board, row, col, self.pieces)
        self.assertEqual([], legals_in_position)
