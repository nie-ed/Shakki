from min_turn import min_turn
from max_turn import max_turn
from point_evaluation import point_evaluation

class Minimax:
    def __init__(self):
        self.scores = []
        self.alph_max = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.alph_min = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.min_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.max_pieces = ["n", "b", "q", "k", "r", "p"]


    def minimax(self, get_legal_moves, list_of_legal_moves, current_depth, is_max_turn, target_depth, trial_board, last_score):
        
        if (current_depth == target_depth):
            return point_evaluation(trial_board)

        if (is_max_turn):
            max_turn(self, get_legal_moves, list_of_legal_moves, current_depth, target_depth, trial_board, last_score)

        else:
            min_turn(self, get_legal_moves, list_of_legal_moves, current_depth, target_depth, trial_board, last_score)

    

