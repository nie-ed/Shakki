class King:
    """Class, which checks the legal moves of a king piece, and adds them to a list.

    """

    def __init__(self):
        pass

    def king_movement(self, board, row, col):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of column on board.
            self_pieces (list): List of the alpabetic characters of columns on the board.
        """

        if board[row][col] == "k":
            is_max_turn = True
            self_pieces = ["n", "b", "q", "k", "r", "p"]
        else:
            is_max_turn = False
            self_pieces = ["N", "B", "Q", "K", "R", "P"]


        xx = row
        yy = col
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        legals = []

        if is_max_turn:
            for i in moves:
                can_be_added_to_legals = True
                x = xx + i[0]
                y = yy + i[1]
                if 0 < x < 9 and 0 <= y < 8:
                    if board[x][y] not in self_pieces:
                        next_x = x
                        next_y = y
                        for n in range(1, 10):
                            next_x =+ i[0]
                            next_y =+ i[1]
                            if 0 < next_x < 9 and 0 <= next_y< 8:
                                # if we are checking laterally or horizontally
                                if next_x == x or next_y == y:
                                    if board[next_x][next_y] == "R" or board[next_x][next_y] == "Q":
                                        can_be_added_to_legals = False
                                        break
                                #if we are checking diagonally
                                else:
                                    # if a opponent pawn is in position to eat
                                    if y - next_y == 1:
                                        if board[next_x][next_y] == "P":
                                            can_be_added_to_legals = False
                                            break
                                    elif board[next_x][next_y] == "B" or board[next_x][next_y] == "Q":
                                        can_be_added_to_legals = False
                                        break  
                                if board[next_x][next_y] in self_pieces:
                                    break
                                if board[next_x][next_y] == ".":
                                    continue
                            else:
                                break
                #lets check that a knight is not thretening the spot
                if can_be_added_to_legals:
                    knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
                    for t, i in knight_moves:
                        if 0 < x + t < 9 and 0 <= y + i < 8:
                            if board[x+t][y+i] == "N":
                                can_be_added_to_legals = False
                                break
                
                if can_be_added_to_legals:
                    legals.append((x,y))

                

        else:
            for i in moves:
                can_be_added_to_legals = True
                x = xx + i[0]
                y = yy + i[1]
                if 0 < x < 9 and 0 <= y < 8:
                    if board[x][y] not in self_pieces:
                        next_x = x
                        next_y = y
                        for n in range(1, 10):
                            next_x =+ i[0]
                            next_y =+ i[1]
                            if 0 < next_x < 9 and 0 <= next_y < 8:
                                # if we are checking laterally or horizontally
                                if next_x == x or next_y == y:
                                    if board[next_x][next_y] == "r" or board[next_x][next_y] == "q":
                                        can_be_added_to_legals = False
                                        break
                                #if we are checking diagonally
                                else:
                                    # if a opponent pawn is in position to eat
                                    if next_y - y == 1:
                                        if board[next_x][next_y] == "p":
                                            can_be_added_to_legals = False
                                            break
                                    elif board[next_x][next_y] == "b" or board[next_x][next_y] == "q":
                                        can_be_added_to_legals = False
                                        break  
                                if board[next_x][next_y] in self_pieces:
                                    break
                                if board[next_x][next_y] == ".":
                                    continue
                            else:
                                break
                
                #lets check that a knight is not thretening the spot
                if can_be_added_to_legals:
                    knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
                    for t, i in knight_moves:
                        if 0 < x + t < 9 and 0 <= y + i < 8:
                            if board[x+t][y+i] == "n":
                                can_be_added_to_legals = False
                                break
                
                if can_be_added_to_legals:
                    legals.append((x,y))

        return legals
