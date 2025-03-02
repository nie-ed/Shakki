def is_king_threatened(board, row, col):
    """Checks if a move to a specific part of the board is okay to do.

    Args:
        board (Board): Board and its state in a list of lists form.
        row (int): Integer value of row on board.
        col (int): Integer value of column on board.
        self_pieces (list): List of the alpabetic characters of columns on the board.
    """

    if board[row][col] == "k":
        is_max_turn = True
        self_pieces = ["n", "b", "q", "r", "p"]
    else:
        is_max_turn = False
        self_pieces = ["N", "B", "Q", "R", "P"]


    x = row
    y = col
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

    if is_max_turn:
        return check_threaths_max_turn(moves, x, y, board, self_pieces, row, col)


    else:
        return check_threaths_min_turn(moves, x, y, board, self_pieces, row, col)


def check_threaths_min_turn(moves, x, y, board, self_pieces, row, col):
    for i in moves:
        next_x = x
        next_y = y
        for n in range(1, 10):
            next_x += i[0]
            next_y += i[1]
            if 0 < next_x < 9 and 0 <= next_y < 8:
                # if we are checking laterally or horizontally
                if next_x == row or next_y == col:
                    if board[next_x][next_y] == "r" or board[next_x][next_y] == "q":
                        return True
                #if we are checking diagonally
                else:
                    # if a opponent pawn is in position to eat
                    if board[next_x][next_y] == "p":
                        if next_x - row == 1 and abs(col - next_y) == 1:
                            return True
                    elif board[next_x][next_y] == "b" or board[next_x][next_y] == "q":
                        return True
                if board[next_x][next_y] in self_pieces:
                    break
            else:
                break
    #if all is good, lets check knight threaths
    return check_knight_min_threaths(x, y, board)

            

def check_threaths_max_turn(moves, x, y, board, self_pieces, row, col):       
    for i in moves:
        #checking if king is threatened in current spot
        #kings current spot
        next_x = x
        next_y = y
        #checking spots that can access kings spot
        for n in range(1, 10):
            next_x += i[0]
            next_y += i[1]
            if 0 < next_x < 9 and 0 <= next_y< 8:
                # if we are checking laterally or horizontally
                if next_x == row or next_y == col:
                    if board[next_x][next_y] == "R" or board[next_x][next_y] == "Q":
                        return True
                #if we are checking diagonally
                else:
                    # if a opponent pawn is in position to eat
                    if board[next_x][next_y] == "P":
                        if row - next_x == 1 and abs(col - next_y) == 1:
                            return True
                    elif board[next_x][next_y] == "B" or board[next_x][next_y] == "Q":
                        return True
                if board[next_x][next_y] in self_pieces:
                    break
            else:
                break
    #if all is good, lets check knight threaths
    return check_knight_max_threaths(x, y, board)


def check_knight_max_threaths(x, y, board):
    #lets check that a knight is not thretening the spot
    knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
    for t, i in knight_moves:
        if 0 < x + t < 9 and 0 <= y + i < 8:
            if board[x+t][y+i] == "N":
                return True
    #if all is good, we can return that the king is noth threatened
    return False


def check_knight_min_threaths(x, y, board):
    #lets check that a knight is not thretening the spot
    knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
    for t, i in knight_moves:
        if 0 < x + t < 9 and 0 <= y + i < 8:
            if board[x+t][y+i] == "n":
                return True
    #if all is good, we can return that the king is noth threatened
    return False

