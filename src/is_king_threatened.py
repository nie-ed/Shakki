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


    king_is_threatened = False
    x = row
    y = col
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

    if is_max_turn:
        for i in moves:
            if king_is_threatened:
                break
            if 0 < x < 9 and 0 <= y < 8:
                next_x = x
                next_y = y
                for n in range(1, 10):
                    next_x += i[0]
                    next_y += i[1]
                    if 0 < next_x < 9 and 0 <= next_y< 8:
                        # if we are checking laterally or horizontally
                        if next_x == x or next_y == y:
                            if board[next_x][next_y] == "R" or board[next_x][next_y] == "Q":
                                king_is_threatened = True
                                break
                        #if we are checking diagonally
                        else:
                            # if a opponent pawn is in position to eat
                            if y - next_y == 1:
                                if board[next_x][next_y] == "P":
                                    king_is_threatened = True
                                    break
                            elif board[next_x][next_y] == "B" or board[next_x][next_y] == "Q":
                                king_is_threatened = True
                                break  
                        if board[next_x][next_y] in self_pieces:
                            break
                        if board[next_x][next_y] == ".":
                            continue
                    else:
                        break
        #lets check that a knight is not thretening the spot
        if not king_is_threatened:
            knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
            for t, i in knight_moves:
                if 0 < x + t < 9 and 0 <= y + i < 8:
                    if board[x+t][y+i] == "N":
                        king_is_threatened = True
                        break

            

    else:
        for i in moves:
            if king_is_threatened:
                break
            if 0 < x < 9 and 0 <= y < 8:
                next_x = x
                next_y = y
                for n in range(1, 10):
                    next_x += i[0]
                    next_y += i[1]
                    if 0 < next_x < 9 and 0 <= next_y < 8:
                        # if we are checking laterally or horizontally
                        if next_x == x or next_y == y:
                            if board[next_x][next_y] == "r" or board[next_x][next_y] == "q":
                                king_is_threatened = True
                                break
                        #if we are checking diagonally
                        else:
                            # if a opponent pawn is in position to eat
                            if next_y - y == 1:
                                if board[next_x][next_y] == "p":
                                    king_is_threatened = True
                                    break
                            elif board[next_x][next_y] == "b" or board[next_x][next_y] == "q":
                                king_is_threatened = True
                                break  
                        if board[next_x][next_y] in self_pieces:
                            break
                        if board[next_x][next_y] == ".":
                            continue
                    else:
                        break
        
        #lets check that a knight is not thretening the spot
        if not king_is_threatened:
            knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
            for t, i in knight_moves:
                if 0 < x + t < 9 and 0 <= y + i < 8:
                    if board[x+t][y+i] == "n":
                        king_is_threatened = True
                        break
            
    return king_is_threatened
