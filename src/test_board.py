class TestBoard:
    def __init__(self, test_board):
        self.test_board = test_board

    def update_board(self, choice, moves):
        first_position_col = moves.index(choice[0])
        first_position_row = int(choice[1])
        second_position_col = moves.index(choice[2])
        second_position_row = int(choice[3])
        piece_moving = self.test_board[first_position_row][first_position_col]
        # if piece_moving != ".":
        # piece eaten
        self.test_board[first_position_row][first_position_col] = "."
        self.test_board[second_position_row][second_position_col] = piece_moving
