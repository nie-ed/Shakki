class Board:
    """The board represented in a list of list form.
    """

    def __init__(self):
        """Class constructor, that creates a new board.
        """
        self.board = [
            [],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]]

    def update_board(self, choice, board_alph):
        """Updates th board with a new move.

        Args:
            choice (str): The move chosen and that should be added to the board.
            board_alph (list): A list ["a", "b", "c", "d", "e", "f", "g", "h"] of the alphabetic values of the columns on the board
        """
        first_position_col = board_alph.index(choice[0])
        first_position_row = int(choice[1])
        second_position_col = board_alph.index(choice[2])
        second_position_row = int(choice[3])
        piece_moving = self.board[first_position_row][first_position_col]
        self.board[first_position_row][first_position_col] = "."
        self.board[second_position_row][second_position_col] = piece_moving
