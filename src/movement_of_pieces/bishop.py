class Bishop:
    """Class, which checks the moves of a bishop piece, and adds them to a list.

    """

    def __init__(self):

        pass

    def bishop_movement(self, board, row, col, self_pieces):
        """Checks if a move to a specific part of the board possible to do.

        Args:
            board (list): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of colum on board.
            self_pieces(list): Alphabetic symbol for own pieces

        Returns:
            list: A list of moves that the bishop can make.
        """


        xx = row
        yy = col
        legals = []

        for i in range(1, len(board)+1):
            x = xx + i
            y = yy + i
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        for i in range(1, len(board)+1):
            x = xx + i
            y = yy - i
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        for i in range(1, len(board)+1):
            x = xx - i
            y = yy + i
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        for i in range(1, len(board)+1):
            x = xx - i
            y = yy - i
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        return legals
