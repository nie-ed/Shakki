class Rook:
    """Class, which checks the possible moves of a rook piece, and adds them to a list.

    """

    def __init__(self):

        pass

    def rook_movement(self, board, row, col, self_pieces):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (list): A boards state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of colum on board.
            self_pieces: Alphabetic symbol for own pieces in a list

         Returns:
            list: A list of moves that the rook can make.
        """


        xx = row
        yy = col
        legals = []

        for i in range(1, len(board)+1):
            x = xx + i
            y = yy
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        for i in range(1, len(board)+1):
            x = xx - i
            y = yy
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        for i in range(1, len(board[1])+1):
            x = xx
            y = yy + i
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        for i in range(1, len(board[1])+1):
            x = xx
            y = yy - i
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] not in self_pieces:
                    legals.append((x, y))
                    if board[x][y] != ".":
                        break
                else:
                    break

        return legals
