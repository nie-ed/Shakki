import unittest
from board import Board
from minimax.minimax import Minimax


class TestCheckmate(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pieces = ["n", "b", "q", "k", "r", "p"]
        self.alph = ["a", "b", "c", "d", "e", "f", "g", "h"]



    def test_ending_checkmate_for_mini_full_flow(self):
            self.board.board = [
                [],
                ["k", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "R", ".", "R", ".", "."],
                [".", ".", "N", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                ["P", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "P", "P"],
                [".", ".", ".", ".", "K", ".", ".", "."]]
            minimax = Minimax()
            depth = 1
            is_max_turn = False
            a = -10000
            b = 10000
            minimax.minimax(depth, is_max_turn, self.board, a, b)
            self.assertEqual(-10000000, minimax.best_move[1])


    def test_ending_checkmate_for_max_full_flow(self):
        self.board.board = [
            [],
            ["P", ".", "P", "P", "K", "P", ".", "P"],
            ["P", "P", "P", "P", "P", "P", ".", "P"],
            [".", ".", "P", ".", ".", "P", ".", "."],
            [".", ".", ".", ".", "P", ".", ".", "q"],
            [".", ".", "b", ".", "p", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", ".", "k", "b", "n", "r"]]
        minimax = Minimax()
        depth = 1
        is_max_turn = True
        a = -10000
        b = 10000
        minimax.minimax(depth, is_max_turn, self.board, a, b)
        self.assertEqual("h4f2", minimax.best_move[0])
        self.assertEqual(10000000, minimax.best_move[1])


    def test_ending_checkmate_for_max_full_flow_2(self):
        self.board.board = [
            [],
            ["R", "N", "B", "Q", "K", "B", ".", "R"],
            ["P", "P", "P", "P", "P", "b", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "N"],
            [".", ".", ".", ".", ".", ".", "n", "q"],
            [".", ".", ".", ".", "p", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", ".", "p", "p", "p"],
            ["r", "n", "b", ".", "k", ".", ".", "r"]]
        minimax = Minimax()
        depth = 2
        is_max_turn = False
        a = -10000
        b = 10000
        minimax.minimax(depth, is_max_turn, self.board, a, b)
        self.assertEqual(1000000, minimax.best_move[1])