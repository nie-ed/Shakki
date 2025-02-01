class Pawn:
    """Class, which checks the legal moves of a pawn piece, and adds them to a list.

    """

    def __init__(self):

        pass

    def pawn_movement(self, board, row, col, opponent_pieces, max_player):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of colum on board.
            opponent_pieces (list): List of opponents pieces in str form. 
        """

        xx = row
        yy = col
        legals = []

        if max_player:

            x = xx - 1
            y = yy
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] == ".":
                    legals.append((x, y))
                    if row == 7 and board[x-1][y] == ".":
                        legals.append((x-1, y))

            x = xx - 1
            y = yy - 1
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] in opponent_pieces:
                    legals.append((x, y))

            x = xx - 1
            y = yy + 1
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] in opponent_pieces:
                    legals.append((x, y))

            return legals
    
        else:
            x = xx + 1
            y = yy
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] == ".":
                    legals.append((x, y))
                    if row == 7 and board[x+1][y] == ".":
                        legals.append((x+1, y))

            x = xx + 1
            y = yy - 1
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] in opponent_pieces:
                    legals.append((x, y))

            x = xx + 1
            y = yy + 1
            if 0 < x < 9 and 0 <= y < 8:
                if board[x][y] in opponent_pieces:
                    legals.append((x, y))

            return legals


        # TO DO
        # if col == 7, change piece type
