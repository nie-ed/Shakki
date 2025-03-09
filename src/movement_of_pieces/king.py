class King:
    """A class that checks what legal moves the king can make and makes a list of them.
    """

    def __init__(self):
        """Class constructor that initiates the needed variables.
        """
        self.legals = []
        self.board = None
        self.king_moves = ((-1, 0), (1, 0), (0, -1), (0, 1),
                           (-1, -1), (-1, 1), (1, -1), (1, 1))

    def king_movement(self, board, row, col, is_max_turn):
        """Finds the legal moved the king can make.

        Args:
            board (list): The current state of the chess board.
            row (int): The row number the king is located at on the board.
            col (_type_): The col number the king is located at on the board.
            is_max_turn (bool): Tells if it is max players turn.

        Returns:
            list : A list of moves the king can legally make.
        """

        self.board = board
        xx = row
        yy = col

        if is_max_turn:
            self_pieces = ["n", "b", "q", "r", "p"]
            for i in self.king_moves:
                x = xx + i[0]
                y = yy + i[1]

                if 0 < x < 9 and 0 <= y < 8:
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
            while True:
                next_x += i[0]
                next_y += i[1]
                if 0 < next_x < 9 and 0 <= next_y < 8:
                    if next_x == x or next_y == y:
                        if self.board[next_x][next_y] == "r" or self.board[next_x][next_y] == "q":
                            return
                        elif self.board[next_x][next_y] == "k":
                            if 0 <= abs(x - next_x) <= 1 and 0 <= abs(y-next_y) <= 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] in ["b", "n", "p", "k"]:
                            break
                    else:
                        if self.board[next_x][next_y] == "p":
                            if next_x - x == 1 and abs(y - next_y) == 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] == "b" or self.board[next_x][next_y] == "q":
                            return
                        elif self.board[next_x][next_y] == "k":
                            if 0 <= abs(x - next_x) <= 1 and 0 <= abs(y-next_y) <= 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] in ["r", "p", "n", "k"]:
                            break
                    if self.board[next_x][next_y] in self_pieces:
                        break
                else:
                    break
        self.check_knight_min_threaths(x, y)

    def check_threats_max_turn(self, self_pieces, i, x, y):
        for i in self.king_moves:
            next_x = x
            next_y = y
            while True:
                next_x += i[0]
                next_y += i[1]
                if 0 < next_x < 9 and 0 <= next_y < 8:
                    if next_x == x or next_y == y:
                        if self.board[next_x][next_y] == "R" or self.board[next_x][next_y] == "Q":
                            return
                        elif self.board[next_x][next_y] == "K":
                            if 0 <= abs(x - next_x) <= 1 and 0 <= abs(y-next_y) <= 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] in ["B", "N", "P", "K"]:
                            break
                    else:
                        if self.board[next_x][next_y] == "P":
                            if x - next_x == 1 and abs(y - next_y) == 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] == "B" or self.board[next_x][next_y] == "Q":
                            return
                        elif self.board[next_x][next_y] == "K":
                            if 0 <= abs(x - next_x) <= 1 and 0 <= abs(y-next_y) <= 1:
                                return
                            else:
                                break
                        elif self.board[next_x][next_y] in ["R", "P", "N", "K"]:
                            break

                    if self.board[next_x][next_y] in self_pieces:
                        break
                else:
                    break
        self.check_knight_max_threaths(x, y)

    def check_knight_min_threaths(self, x, y):
        knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2),
                        (2, -1), (2, 1), (1, 2), (1, -2))
        for t, i in knight_moves:
            if 0 < x + t < 9 and 0 <= y + i < 8:
                if self.board[x+t][y+i] == "n":
                    return
        self.legals.append((x, y))

    def check_knight_max_threaths(self, x, y):
        knight_moves = ((-2, -1), (-2, 1), (-1, 2), (-1, -2),
                        (2, -1), (2, 1), (1, 2), (1, -2))
        for t, i in knight_moves:
            if 0 < x + t < 9 and 0 <= y + i < 8:
                if self.board[x+t][y+i] == "N":
                    return
        self.legals.append((x, y))
