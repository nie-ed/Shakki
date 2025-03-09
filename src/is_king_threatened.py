def is_king_threatened(board, row, col):
    """Checks if a move will make own king threatened or not.

    Args:
        board (list): The boards state in a list of lists form.
        row (int): Integer value of row on board where king is located.
        col (int): Integer value of column on boardwhere king is located.

    Returns:
        bool : Tells if the king is threatened or not.
    """

    if board[row][col] == "k":
        is_max_turn = True
        self_pieces = ["n", "b", "q", "r", "p"]
    else:
        is_max_turn = False
        self_pieces = ["N", "B", "Q", "R", "P"]

    x = row
    y = col
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1),
             (-1, -1), (-1, 1), (1, -1), (1, 1))

    if is_max_turn:
        return check_threats_max_turn(moves, x, y, board, self_pieces, row, col)

    return check_threats_min_turn(moves, x, y, board, self_pieces, row, col)


def check_threats_min_turn(moves, x, y, board, self_pieces, row, col):
    """Checks for min player if a move will make own king threatened or not.

    Args:
        moves (list): List of integer pairs for traversing the board.
        x (int): Integer value of row on board where king is located.
        y (int): Integer value of column on boardwhere king is located.
        board (list): The boards state in a list of lists form.
        self_pieces (_type_): _description_
        row (int): Integer value of row on board where king is located.
        col (int): Integer value of column on boardwhere king is located.

    Returns:
        bool : Tells if the king is threatened or not.
    """

    for i in moves:
        next_x = x
        next_y = y
        while True:
            next_x += i[0]
            next_y += i[1]
            if 0 < next_x < 9 and 0 <= next_y < 8:
                if next_x == row or next_y == col:
                    if board[next_x][next_y] == "r" or board[next_x][next_y] == "q":
                        return True
                    elif board[next_x][next_y] == "k":
                        if 0 <= abs(x - next_x) and abs(x-next_x) <= 1 and 0 <= abs(y-next_y) and abs(y-next_y) <= 1:
                            return True
                        else:
                            break
                    elif board[next_x][next_y] in ["b", "n", "p", "k"]:
                        break
                else:
                    if board[next_x][next_y] == "p":
                        if next_x - row == 1 and abs(col - next_y) == 1:
                            return True
                        else:
                            break
                    elif board[next_x][next_y] == "b" or board[next_x][next_y] == "q":
                        return True
                    elif board[next_x][next_y] == "k":
                        if 0 <= abs(x - next_x) and abs(x-next_x) <= 1 and 0 <= abs(y-next_y) and abs(y-next_y) <= 1:
                            return True
                        else:
                            break
                    elif board[next_x][next_y] in ["r", "p", "n", "k"]:
                        break
                if board[next_x][next_y] in self_pieces:
                    break
            else:
                break
    return check_knight_min_threaths(x, y, board)


def check_threats_max_turn(moves, x, y, board, self_pieces, row, col):
    """Checks for max player if a move will make own king threatened or not.

    Args:
        moves (list): List of integer pairs for traversing the board.
        x (int): Integer value of row on board where king is located.
        y (int): Integer value of column on boardwhere king is located.
        board (list): The boards state in a list of lists form.
        self_pieces (_type_): _description_
        row (int): Integer value of row on board where king is located.
        col (int): Integer value of column on boardwhere king is located.

    Returns:
        bool : Tells if the king is threatened or not.
    """

    for i in moves:
        next_x = x
        next_y = y
        while True:
            next_x += i[0]
            next_y += i[1]
            if 0 < next_x < 9 and 0 <= next_y < 8:
                if next_x == row or next_y == col:
                    if board[next_x][next_y] == "R" or board[next_x][next_y] == "Q":
                        return True
                    elif board[next_x][next_y] == "K":
                        if 0 <= abs(x - next_x) and abs(x-next_x) <= 1 and 0 <= abs(y-next_y) and abs(y-next_y) <= 1:
                            return True
                        else:
                            break
                    elif board[next_x][next_y] in ["B", "N", "P", "K"]:
                        break
                else:
                    if board[next_x][next_y] == "P":
                        if row - next_x == 1 and abs(col - next_y) == 1:
                            return True
                        else:
                            break
                    elif board[next_x][next_y] == "B" or board[next_x][next_y] == "Q":
                        return True
                    elif board[next_x][next_y] == "K":
                        if 0 <= abs(x - next_x) <= 1 and 0 <= abs(y-next_y) <= 1:
                            return True
                        else:
                            break
                    elif board[next_x][next_y] in ["R", "P", "N", "K"]:
                        break
                if board[next_x][next_y] in self_pieces:
                    break
            else:
                break
    return check_knight_max_threaths(x, y, board)


def check_knight_max_threaths(x, y, board):
    """Check if the max king is threatened by knight

    Args:
        x (int): Integer value of row on board where king is located.
        y (int): Integer value of column on boardwhere king is located.
        board (list): The boards state in a list of lists form.

    Returns:
        bool : Tells if the king is threatened or not.
    """

    knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2),
                    (2, -1), (2, 1), (1, 2), (1, -2))
    for t, i in knight_moves:
        if 0 < x + t < 9 and 0 <= y + i < 8:
            if board[x+t][y+i] == "N":
                return True
    return False


def check_knight_min_threaths(x, y, board):
    """Check if the min king is threatened by knight

    Args:
        x (int): Integer value of row on board where king is located.
        y (int): Integer value of column on boardwhere king is located.
        board (list): The boards state in a list of lists form.

    Returns:
        bool : Tells if the king is threatened or not.
    """

    knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2),
                    (2, -1), (2, 1), (1, 2), (1, -2))
    for t, i in knight_moves:
        if 0 < x + t < 9 and 0 <= y + i < 8:
            if board[x+t][y+i] == "n":
                return True
    return False
