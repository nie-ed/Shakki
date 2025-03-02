class Board:
    def __init__(self):
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

    def update_board(self, choice, moves):
        first_position_col = moves.index(choice[0])
        first_position_row = int(choice[1])
        second_position_col = moves.index(choice[2])
        second_position_row = int(choice[3])
        piece_moving = self.board[first_position_row][first_position_col]
        self.board[first_position_row][first_position_col] = "."
        if piece_moving == "p" and second_position_row == 1:
            self.board[second_position_row][second_position_col] = "q"
        else:
            self.board[second_position_row][second_position_col] = piece_moving


