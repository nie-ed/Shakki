import copy
import math


def max_turn(self, get_legal_moves, list_of_legal_moves, current_depth, target_depth, trial_board, last_score):
    maxi = -math.inf
    for i, move in enumerate(list_of_legal_moves):
        print(f"test board now: last move was mins{trial_board.trial_board}")
        new_trial_board = copy.deepcopy(trial_board)
        new_trial_board.update_board(move, self.alph_max)
        print(f"test board now: new move by max{new_trial_board.trial_board}")

        new_list_of_legal_moves = get_legal_moves(
            new_trial_board.trial_board, False)
        
        score_now = self.minimax(get_legal_moves, new_list_of_legal_moves, current_depth + 1, 
                                        False, target_depth, new_trial_board, last_score)
        real_score = max(score_now, maxi)
        self.scores[i] = real_score
        print(f"score now: {score_now}")
    return real_score