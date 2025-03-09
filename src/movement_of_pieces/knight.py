class Knight():
    """Class, which checks the moves of a knight piece, and adds them to a list.

    """

    def __init__(self):
        pass

    def knight_movement(self, board, row, col, self_pieces):
        """Checks if a move to a specific part of the board possible to do.

        Args:
            board (list): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of column on board.
            self_pieces(list): Alphabetic symbol for own pieces

        Returns:
            list: A list of moves that the bishop can make.
        """

        xx = row
        yy = col
        moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2),
                 (2, -1), (2, 1), (1, 2), (1, -2))
        legals = []

        for i in moves:
            x = xx + i[0]
            y = yy + i[1]
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))

        return legals
