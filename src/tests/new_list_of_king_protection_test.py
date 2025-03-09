import unittest
from is_king_threatened import is_king_threatened
from get_legal_moves import get_legal_moves
from board import Board
from minimax.minimax import Minimax
import copy


class TestList(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pieces = ["n", "b", "q", "k", "r", "p"]
        self.alph = ["a", "b", "c", "d", "e", "f", "g", "h"]


# max turn

    def test_max_rook_protect_king(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", "p", "r", "p", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "p", ".", ".", "."],
            ["R", ".", ".", "p", "k", ".", ".", "R"],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", ".", ".", ".", ".", "p", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]]
        row = 4
        col = 4
        list_of_moves = get_legal_moves(self.board.board , True)
        self.assertCountEqual(["e3e2", "f1f2", "f1f3", "f1f4", "f1f5", "f6f5", "d4d3"], list_of_moves)
        legals = stub_only_moves_that_protect_the_king(self.board, list_of_moves, row, col, self.alph)
        self.assertCountEqual(["f1f4"], legals)


    def test_max_bishop_protect_king(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", "p", ".", "p", "."],
            [".", ".", ".", ".", ".", ".", ".", "b"],
            [".", ".", ".", ".", "p", ".", ".", "."],
            ["R", ".", ".", "p", "k", ".", ".", "R"],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", "p", ".", "p", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]]
        row = 4
        col = 4
        list_of_moves = get_legal_moves(self.board.board , True)
        self.assertCountEqual(["e3e2", "h2g3", "h2f4", "h2e5", "f6f5", "d4d3"], list_of_moves)
        legals = stub_only_moves_that_protect_the_king(self.board, list_of_moves, row, col, self.alph)
        self.assertCountEqual(["h2f4"], legals)

    def test_max_king_is_not_protected_checkmate(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", ".", ".", "k", ".", ".", "R"],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]]
        minimax = Minimax()
        depth = 1
        is_max_turn = True
        a = 0
        b = 0
        score = minimax.minimax(depth, is_max_turn, self.board, a, b)
        self.assertEqual(-10000000, score)



# min turn

    def test_min_rook_protect_king(self):
            self.board.board = [
                [],
                [".", ".", ".", ".", "P", "R", "P", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", "P", ".", ".", "."],
                ["r", ".", ".", "P", "K", ".", ".", "r"],
                [".", ".", ".", ".", "P", ".", ".", "."],
                [".", ".", ".", ".", ".", "P", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."]]
            row = 4
            col = 4
            list_of_moves = get_legal_moves(self.board.board, False)
            self.assertCountEqual(["e1e2", "f6f7", "f1f2", "f1f3", "f1f4", "f1f5", "d4d5", "g1g2", "e5e6"], list_of_moves)
            legals = stub_only_moves_that_protect_the_king(self.board, list_of_moves, row, col, self.alph)
            self.assertCountEqual(["f1f4"], legals)


    def test_min_bishop_protect_king(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "B"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["r", ".", ".", "P", "K", ".", ".", "r"],
            [".", ".", ".", ".", "P", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]]
        row = 4
        col = 4
        list_of_moves = get_legal_moves(self.board.board , False)
        self.assertCountEqual(["d4d5", "h2g3", "h2f4", "e5e6", "h2g1"], list_of_moves)
        legals = stub_only_moves_that_protect_the_king(self.board, list_of_moves, row, col, self.alph)
        self.assertCountEqual(["h2f4"], legals)


    def test_min_king_is_not_protected_checkmate(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "r"],
            [".", ".", ".", ".", "K", ".", ".", "r"],
            [".", ".", ".", ".", ".", ".", ".", "r"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."]]
        minimax = Minimax()
        depth = 1
        is_max_turn = False
        a = 0
        b = 0
        score = minimax.minimax(depth, is_max_turn, self.board, a, b)
        self.assertEqual(10000000, score)




# STUB FUNCTION
def stub_only_moves_that_protect_the_king(board, new_list_of_legal_moves, row, col, alph):
    unchecked_new_list_of_legal_moves = new_list_of_legal_moves
    new_list_of_legal_moves = []

    for move in unchecked_new_list_of_legal_moves:
        earlier_board = copy.deepcopy(board.board)
        board.update_board(move, alph)                
        does_king_end_up_threatened = is_king_threatened(board.board, row, col)
        if does_king_end_up_threatened is False:
            new_list_of_legal_moves.append(move)
        board.board = earlier_board
        earlier_board = None

    return new_list_of_legal_moves