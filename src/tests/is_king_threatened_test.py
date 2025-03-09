import unittest
from is_king_threatened import is_king_threatened


class TestThreath(unittest.TestCase):

    # max king tests

    def test_king_threatened_from_up(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "B", "N", "R"],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threatened_from_down(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", ".", "B", "N", "R"],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "R", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_from_up_blocked_by_own(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "B", "N", "R"],
            ["P", "P", "P", "P", "n", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_pawn(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "B", "N", "R"],
            ["P", "P", "P", ".", "P", "P", "P", "P"],
            [".", ".", ".", "P", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_by_pawn_from_left(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", "P", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_diagonal(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_diagonal_blocked_by_opposition_piece(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", "K", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king_diagonally(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", "K", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king_diagonally_but_opponent_king_too_far(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "K", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king_but_opponent_king_too_far(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", "K", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_knight(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", "N", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))


# min king tests

    def test_king_threatened_from_up_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "r", "B", "N", "R"],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threatened_from_down_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", ".", "B", "N", "R"],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "r", "p", "p", "p"],
            ["r", "n", "b", "q", ".", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_from_up_blocked_by_own_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", ".", "B", "N", "R"],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "N", "p", "p", "p"],
            ["r", "n", "b", "q", "r", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_pawn_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "B", "N", "R"],
            ["P", "P", "P", ".", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_by_pawn_from_left_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", "p", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_diagonal_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", ".", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "b", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_diagonal_blocked_by_opposition_piece_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "b", "n", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", "k", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king_diagonally_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", "k", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king_diagonally_but_opponent_king_too_far_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "k", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_opponent_king_but_opponent_king_too_far_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", "k", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(False, is_king_threatened(test_board, row, col))

    def test_king_threat_by_knight_min(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", "n", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        self.assertEqual(True, is_king_threatened(test_board, row, col))
