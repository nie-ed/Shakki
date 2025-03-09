import unittest
from movement_of_pieces.pawn import Pawn


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.pawn = Pawn()
        self.opponent_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.pieces = ["n", "b", "q", "k", "r", "p"]

    def test_own_pawn_cannot_move(self):
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
        row = 8
        col = 4
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, self.opponent_pieces, True)
        self.assertEqual([], legals_in_position)

    def test_own_pawn_can_move_one_up(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 5
        col = 4
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, self.opponent_pieces, True)
        self.assertEqual([(4, 4)], legals_in_position)

    def test_own_pawn_can_move_two_up(self):
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
        row = 7
        col = 4
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, self.opponent_pieces, True)
        self.assertEqual([(6, 4), (5, 4)], legals_in_position)

    def test_own_pawn_can_move_diagonally_on_opponent(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", ".", "P", ".", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", ".", ".", "P", ".", "P", ".", "."],
            ["p", "p", "p", ".", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 7
        col = 4
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, self.opponent_pieces, True)
        self.assertEqual([(6, 4), (6, 3), (6, 5)], legals_in_position)

    def test_own_pawn_if_row_and_col_go_past_board(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", ".", "P", ".", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", ".", ".", "P", ".", "P", ".", "."],
            ["p", "p", "p", ".", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 9
        col = 9
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, self.opponent_pieces, True)
        self.assertEqual([], legals_in_position)

    def test_opponent_pawn_cannot_move(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "P", "B", "N", "R"],
            ["P", "P", "P", "P", "K", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 1
        col = 4
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, self.pieces, False)
        self.assertEqual([], legals_in_position)

    def test_opponent_pawn_can_move_one_up(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", ".", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "P", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 2
        col = 4
        opponent_pieces = self.pieces
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, opponent_pieces, False)
        self.assertEqual([(3, 4)], legals_in_position)

    def test_opponent_pawn_can_move_two_up(self):
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
        row = 2
        col = 4
        opponent_pieces = self.pieces
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, opponent_pieces, False)
        self.assertEqual([(3, 4), (4, 4)], legals_in_position)

    def test_opponent_pawn_can_move_diagonally_on_opponent(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", ".", "P", "P", "P", "P"],
            [".", ".", ".", "p", ".", "p", ".", "."],
            [".", ".", ".", ".", "P", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", ".", "p", ".", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 2
        col = 4
        opponent_pieces = self.pieces
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, opponent_pieces, False)
        self.assertEqual([(3, 4), (3, 3), (3, 5)], legals_in_position)

    def test_opponent_pawn_if_row_and_col_go_past_board(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", ".", "P", ".", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", ".", ".", "P", ".", "P", ".", "."],
            ["p", "p", "p", ".", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 9
        col = 9
        opponent_pieces = self.pieces
        legals_in_position = self.pawn.pawn_movement(
            test_board, row, col, opponent_pieces, False)
        self.assertEqual([], legals_in_position)
