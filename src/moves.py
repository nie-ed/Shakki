from minimax.minimax import Minimax


class Moves:
    """Class, which creates the objects for the piece movement checking and calls the fuctions to check for legal moves.
    """

    def __init__(self):
        self.moves_made_earlier = []
        self.min_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.max_pieces = ["n", "b", "q", "k", "r", "p"]
        self.min_alph = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.max_alph = ["a", "b", "c", "d", "e", "f", "g", "h"]

    

    def make_move(self, board):
        """Calls the method which checks the legal moves of a piece.

        Args:
            board (Board): Board and its state in a list of lists form.

        Returns:
            str: The chocen move to make, in string form and a for the AI platform can understand.
        """
        minimax_object = Minimax()
        minimax_algorithm = minimax_object.minimax
        current_depth = 2
        a = -10000
        b = 10000

        minimax_algorithm(current_depth, True, board, a, b)
        if minimax_object.best_move:
            print(f"best moves: {minimax_object.best_move}")
            choice = minimax_object.best_move[0]
            return choice
