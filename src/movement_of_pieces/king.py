class King:
    """Class, which checks the legal moves of a king piece, and adds them to a list.

    """

    def __init__(self):
        pass

    def king_movement(self, board, row, col, self_pieces):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of column on board.
            self_pieces (list): List of the alpabetic characters of columns on the board.
        """

        xx = row
        yy = col
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        legals = []

        for i in moves:
            x = xx + i[0]
            y = yy + i[1]
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))

        return legals
