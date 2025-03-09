import unittest
from movement_of_pieces.king import King

class TestKing(unittest.TestCase):
    def setUp(self):
        self.king = King()
        self.pieces = ["n", "b", "q", "k", "r", "p"]


# max king tests:

    def test_king_cannot_max_move(self):
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
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([], legals_in_position)

    def test_max_king_cannot_move_checkmate(self):
        test_board = [
            [],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", ".", ".", "k", ".", ".", "R"],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]]
        row = 4
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([], legals_in_position)

    def test_max_king_can_move_anyway(self):
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
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([(4, 4), (6, 4), (5, 3), (5, 5), (4, 3), (4, 5), (6, 3), (6, 5)], legals_in_position)

    def test_max_king_can_move_down(self):
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
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([(8, 4)], legals_in_position)

    def test_max_king_can_move_up_and_diagonally_up(self):
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
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([(6, 4), (6, 3), (6, 5)], legals_in_position)

    def test_max_king_cannot_move_where_rook_threath(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 7
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([], legals_in_position)

    def test_max_king_cannot_move_where_queen_threath(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "r", "B", "N", "."],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "k", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "Q", ".", ".", "R"],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([(4, 3), (4, 5)], legals_in_position)

    def test_max_king_cannot_move_where_pawn_threath(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "P", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 7
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([(6, 4)], legals_in_position)

    def test_max_king_cannot_move_where_diagonal_threath(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "B", "."],
            [".", ".", ".", ".", ".", ".", "Q", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 7
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([(6, 3)], legals_in_position)

    def test_max_king_movement_blocked_by_opposing_king(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "R", "R", "P", "B"],
            ["P", "P", "P", "P", "K", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "K", ".", "k", ".", "K", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 4
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, True)
        self.assertEqual([], legals_in_position)




# min king tests:

    def test_min_king_cannot_move(self):
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
        row = 1
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, False)
        self.assertEqual([], legals_in_position)

    def test_min_king_can_move_anyway(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", ".", "B", "N", "R"],
            ["P", "P", "P", "P", ".", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "K", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 4
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, False)
        self.assertCountEqual([(3, 3), (3, 4), (3, 5), (4, 5), (4, 3), (5, 3), (5, 4), (5, 5)], legals_in_position)


    def test_min_king_can_move_down(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", ".", "B", "N", "R"],
            ["P", "P", "P", "P", "K", "P", "P", "P"],
            [".", ".", ".", "P", "P", "P", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "p", ".", "."],
            ["p", "p", "p", "p", "p", "p", ".", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 2
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, False)
        self.assertEqual([(1, 4)], legals_in_position)

    def test_min_king_can_move_up_and_diagonally_up(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "P", "B", "N", "R"],
            ["P", "P", "P", "P", "K", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]
        row = 2
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, False)
        self.assertEqual([(3, 4), (3, 3), (3, 5)], legals_in_position)

    def test_min_king_cannot_move_where_rook_threath(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "P", "B", "N", "R"],
            ["P", "P", "P", "P", "K", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "r"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 2
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, False)
        self.assertEqual([], legals_in_position)

    def test_min_king_cannot_move_where_pawn_threath(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "P", "B", "N", "R"],
            ["P", "P", "P", "P", "K", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 2
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, False)
        self.assertEqual([(3, 4)], legals_in_position)

    def test_min_king_cannot_move_where_diagonal_threath(self):
        test_board = [
            [],
            ["R", "N", "B", "Q", "P", "B", "N", "R"],
            ["P", "P", "P", "P", "K", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "b", "q", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "k", "p", "p", "p"],
            ["r", "n", "b", "q", "p", "b", "n", "r"]]
        row = 2
        col = 4
        legals_in_position = self.king.king_movement(test_board, row, col, False)
        self.assertEqual([(3, 5)], legals_in_position)