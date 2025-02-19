from minimax.point_evaluation import point_evaluation
from get_legal_moves import get_legal_moves
import copy



class Minimax:
    def __init__(self):
        self.alph = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.best_move= None

    def minimax(self, current_depth, is_max_turn, board):
        

        
        if (current_depth == 0):
            score = point_evaluation(board)
            return score

        new_list_of_legal_moves = []
        new_list_of_legal_moves = get_legal_moves(board.board, is_max_turn)

        if (is_max_turn):
            maxi = -1000000
            last_best_move = None
            for move in new_list_of_legal_moves:
                earlier_board = copy.deepcopy(board.board)
                board.update_board(move, self.alph)                
                score_now = self.minimax(current_depth - 1, False, board)
                if max(score_now, maxi) == score_now:
                    maxi = max(score_now, maxi)
                    last_best_move = move
                self.best_move = (last_best_move, maxi)
                board.board = earlier_board
            return maxi


        else:
            mini = 1000000
            last_best_move = None
            for move in new_list_of_legal_moves:
                earlier_board = copy.deepcopy(board.board)
                board.update_board(move, self.alph)                
                score_now = self.minimax(current_depth - 1, True, board)
                if min(score_now, mini) == score_now:
                    mini = min(score_now, mini)
                    last_best_move = move
                self.best_move = (last_best_move, mini)
                board.board = earlier_board
            return mini



        



