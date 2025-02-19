import copy
import math


def max_turn(self, get_legal_moves, list_of_legal_moves, current_depth, trial_board):
    maxi = -math.inf
    for move in list_of_legal_moves:
        print(f"test board now: last move was mins{trial_board.trial_board}")
        new_trial_board = copy.deepcopy(trial_board)
        new_trial_board.update_board(move, self.alph_max)
        print(f"test board now: new move by max{new_trial_board.trial_board}")

        new_list_of_legal_moves = get_legal_moves(
            new_trial_board.trial_board, False)
        
        score_now = self.minimax(current_depth - 1, False, new_trial_board)
        print(f"score now: {score_now}")

        maxi = max(score_now, maxi)
        self.scores.update({move: maxi})
    return maxi