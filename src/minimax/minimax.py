from minimax.point_evaluation import point_evaluation
from minimax.min_turn import min_turn
from minimax.max_turn import max_turn


class Minimax:
    def __init__(self):
        self.scores = {}
        self.alph_max = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.min_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.max_pieces = ["n", "b", "q", "k", "r", "p"]


    def minimax(self, get_legal_moves, list_of_legal_moves, current_depth, is_max_turn, trial_board):
        
        if (current_depth == 2):
            score = point_evaluation(trial_board)
            print(f"new score: {score}")
            return score

        elif (is_max_turn):
            return max_turn(self, get_legal_moves, list_of_legal_moves, current_depth, trial_board)

        else:
            return min_turn(self, get_legal_moves, list_of_legal_moves, current_depth, trial_board)




        



