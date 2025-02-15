import copy
import math

def min_turn(self, get_legal_moves, list_of_legal_moves, current_depth, trial_board):
    mini = math.inf
    for move in list_of_legal_moves:
        print(f"test board now: last move was maxes {trial_board.trial_board}")
        new_trial_board = copy.deepcopy(trial_board)
        new_trial_board.update_board(move, self.alph_max)
        print(f"test board now: new move by min{new_trial_board.trial_board}")

        new_list_of_legal_moves = get_legal_moves(
            new_trial_board.trial_board, True)

        score_now = self.minimax(get_legal_moves, new_list_of_legal_moves, current_depth + 1,
                        True, new_trial_board)
        print(f"score_now: {score_now}")
        mini= min(score_now, mini)
    return mini
