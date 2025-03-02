class King:
    """Class, which checks the legal self.king_moves of a king piece, and adds them to a list.

    """

    def __init__(self):
        self.legals = []
        self.board = None
        self.king_moves = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))


    def king_movement(self, board, row, col, is_max_turn):
        """Checks if a move to a specific part of the self.board is okay to do.

        Args:
            self.board (self.Board): self.Board and its state in a list of lists form.
            row (int): Integer value of row on self.board.
            col (int): Integer value of column on self.board.
            self_pieces (list): List of the alpabetic characters of columns on the self.board.
        """

        self.board = board
        xx = row
        yy = col
        print(f"origin x {xx} origin y {yy}")

        if is_max_turn:
            self_pieces = ["n", "b", "q", "r", "p"]
            for i in self.king_moves:
                #this is the move we are checking now, move here as king and check, if this position is threatened
                x = xx + i[0]
                y = yy + i[1]
                print(f"next move x {x} y {y}")

                #if spot in self.board and not occupied by own piece, looks like can be so far added to list of legals, still need to check if that position is treatened
                if 0 < x < 9 and 0 <= y < 8:
                    print(self.board[x][y])
                    if self.board[x][y] not in self_pieces:
                        self.check_threats_max_turn(self_pieces, i, x, y)
           

        else:
            self_pieces = ["N", "B", "Q", "R", "P"]
            for i in self.king_moves:
                x = xx + i[0]
                y = yy + i[1]
                if 0 < x < 9 and 0 <= y < 8:
                    if self.board[x][y] not in self_pieces:
                        self.check_threats_min_turn(self_pieces, i, x, y)
        
        return self.legals



    def check_threats_min_turn(self, self_pieces, i, x, y):
        for i in self.king_moves:
            next_x = x
            next_y = y
            for n in range(1, 10):
                next_x += i[0]
                next_y += i[1]
                if 0 < next_x < 9 and 0 <= next_y < 8:
                    # if we are checking laterally or horizontally
                    if next_x == x or next_y == y:
                        if self.board[next_x][next_y] == "r" or self.board[next_x][next_y] == "q":
                            return
                        elif self.board[next_x][next_y] == "k":
                            if abs(x - next_x) == 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] != ".":
                            break
                    #if we are checking diagonally
                    else:
                        # if a opponent pawn is in position to eat
                        if self.board[next_x][next_y] == "p":
                            if next_x - x == 1 and abs(y - next_y) == 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] == "b" or self.board[next_x][next_y] == "q":
                            return
                        elif self.board[next_x][next_y] == "k":
                            if abs(x - next_x) == 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] != ".":
                            break
                    if self.board[next_x][next_y] in self_pieces:
                        break
                else:
                    break
        self.check_knight_min_threaths(x, y)


    def check_threats_max_turn(self, self_pieces, i, x, y):
        #lets check, if it is a threatened 
        for i in self.king_moves:
            #spot we are at now
            next_x = x
            next_y = y
            #lets check the spots that could access our kings new spot
            for n in range(0, 10):
                next_x += i[0]
                next_y += i[1]
                print(f"next x{next_x} next y {next_y}")
                if 0 < next_x < 9 and 0 <= next_y< 8:
                    # if we are checking laterally or horizontally, so either x or y stays the same
                    if next_x == x or next_y == y:
                        if self.board[next_x][next_y] == "R" or self.board[next_x][next_y] == "Q":
                            return
                        elif self.board[next_x][next_y] == "K":
                            if abs(x - next_x) == 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] != ".":
                            break
                    #if we are checking diagonally
                    else:
                        # if a opponent pawn is in position to eat
                        if self.board[next_x][next_y] == "P":
                            if x - next_x == 1 and abs(y - next_y) == 1:
                                return
                            else:
                                break
                            #check other diagonally moving pieces
                        elif self.board[next_x][next_y] == "B" or self.board[next_x][next_y] == "Q":
                            return
                        elif self.board[next_x][next_y] == "K":
                            if abs(x - next_x) == 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] != ".":
                            break

                    #if a spot is occupied by own piece, that piece protects from that angle
                    if self.board[next_x][next_y] in self_pieces:
                        break
                else:
                    break
        self.check_knight_max_threaths(x, y)


    def check_knight_min_threaths(self, x, y):
        #lets check that a knight is not thretening the spot
        knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
        for t, i in knight_moves:
            if 0 < x + t < 9 and 0 <= y + i < 8:
                if self.board[x+t][y+i] == "n":
                    return
        #if all is good, we add to list of legals
        print(f"adding to legals {x, y}")
        self.legals.append((x, y))

    def check_knight_max_threaths(self, x, y):
        #lets check that a knight is not thretening the spot
        knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, 2), (1, -2))
        for t, i in knight_moves:
            if 0 < x + t < 9 and 0 <= y + i < 8:
                if self.board[x+t][y+i] == "N":
                    return
        #if all is good, we add to list of legals
        print(f"adding to legals {x, y}")
        self.legals.append((x, y))
