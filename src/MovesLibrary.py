from board import Board
from minimax.minimax import Minimax
from moves import Moves

class MovesLibrary:
    def __init__(self):
        self._minimax = Minimax()
        self.board = Board()
        self._moves = Moves()
        self.board_alph = ["a", "b", "c", "d", "e", "f", "g", "h"]



    def checkmate_4_moves(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", "r", ".", "N", "R"],
            [".", "P", "p", "K", "N", "P", "P", "P"],
            [".", ".", ".", ".", "P", ".", ".", "."],
            [".", "n", ".", "P", "n", "B", ".", "."],
            [".", ".", ".", "p", ".", ".", ".", "."],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", "p", "p", ".", ".", "p", "p", "p"],
            [".", ".", ".", "k", "B", ".", ".", "r"]]
        depth = 4
        is_max_turn = False
        a = -10000
        b = 10000
        self._minimax.minimax(depth, is_max_turn, self.board, a, b)


    def checkmate_3_moves(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", "r", ".", "b", "."],
            [".", "p", ".", ".", ".", ".", "B", "."],
            ["p", "N", ".", ".", "p", "R", ".", "."],
            ["R", "B", ".", ".", "k", ".", ".", "."],
            [".", "P", ".", ".", "N", ".", ".", "p"],
            [".", ".", "p", ".", ".", ".", "b", "."],
            ["n", ".", ".", "P", ".", "p", ".", "r"],
            [".", ".", ".", ".", ".", "K", ".", "n"]]
        depth = 3
        is_max_turn = False
        a = -10000
        b = 10000
        self._minimax.minimax(depth, is_max_turn, self.board, a, b)


    def checkmate_2_moves(self):
        self.board.board = [
            [],
            [".", ".", ".", ".", ".", "R", "K", "."],
            [".", ".", ".", "P", ".", "P", "P", "P"],
            [".", ".", "N", ".", ".", ".", ".", "."],
            [".", ".", "B", ".", "P", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "Q"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "p", "p", "p", "p", "h"],
            ["r", ".", ".", "q", "k", "b", "n", "r"]]
        depth = 2
        is_max_turn = False
        a = -10000
        b = 10000
        self._minimax.minimax(depth, is_max_turn, self.board, a, b)


    def minimax_best_score_should_be(self, expected):
        int_expected = int(expected)
        if self._minimax.best_move[1] != int_expected:
            raise AssertionError(f"{self._minimax.best_move[1] != {int_expected}}")