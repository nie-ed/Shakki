from minimax.minimax import Minimax


class Moves:
    """Class, which calls the function that initiates the minimax algorithim. 
    """

    def __init__(self):
        pass

    def make_move(self, board):
        """Calls the fuction that has the minimax algorithmin

        Args:
            board (Board): Board object and its state in a list of lists form.

        Returns:
            tuple: The chosen move to make and its score.
        """
        minimax_object = Minimax()
        minimax_algorithm = minimax_object.minimax
        current_depth = 4
        alpha = -10000
        beta = 10000

        minimax_algorithm(current_depth, True, board, alpha, beta)
        return minimax_object.best_move
