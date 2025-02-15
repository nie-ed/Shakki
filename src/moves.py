from movement_of_pieces.knight import Knight
from movement_of_pieces.pawn import Pawn
from movement_of_pieces.king import King
from movement_of_pieces.rook import Rook
from movement_of_pieces.bishop import Bishop
from movement_of_pieces.queen import Queen
from minimax import Minimax
from trial_board import TrialBoard


class Moves:
    """Class, which creates the objects for the piece movement checking and calls the fuctions to check for legal moves.
    """

    def __init__(self):
        self.moves_made_earlier = []
        self.min_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.max_pieces = ["n", "b", "q", "k", "r", "p"]
        self.min_alph = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.max_alph = ["a", "b", "c", "d", "e", "f", "g", "h"]

    

    def make_move(self, board):
        """Calls the method which checks the legal moves of a piece.

        Args:
            board (Board): Board and its state in a list of lists form.

        Returns:
            str: The chocen move to make, in string form and a for the AI platform can understand.
        """
        legals = self.get_legal_moves(board, True)

        minimax_object = Minimax()
        minimax_algorithm = minimax_object.minimax
        minimax_object.scores = [0] * len(legals)
        trial_board = TrialBoard(board.copy())

        minimax_algorithm(self.get_legal_moves, legals, 0, True, 1, trial_board, 0)

        print(f"legals: {legals}")

        choice = legals[minimax_object.scores.index(max(minimax_object.scores))]
        print(minimax_object.scores)


        return choice


    def get_legal_moves(self, board, max_player):
        knight = Knight()
        pawn = Pawn()
        king = King()
        rook = Rook()
        bishop = Bishop()
        queen = Queen()

        legals = []

        if max_player:
            for row in range(len(board)):
                for col in range(len(board[row])):

                    if board[row][col] == "p":
                        added_legals = pawn.pawn_movement(
                            board, row, col, self.min_pieces, True)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "n":
                        added_legals = knight.knight_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "k":
                        added_legals = king.king_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "r":
                        added_legals = rook.rook_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "b":
                        added_legals = bishop.bishop_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "q":
                        added_legals = queen.queen_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

        
        else:
            for row in range(len(board)):
                for col in range(len(board[row])):

                    if board[row][col] == "P":
                        added_legals = pawn.pawn_movement(
                            board, row, col, self.min_pieces, False)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "N":
                        added_legals = knight.knight_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "K":
                        added_legals = king.king_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "R":
                        added_legals = rook.rook_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "B":
                        added_legals = bishop.bishop_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")

                    if board[row][col] == "Q":
                        added_legals = queen.queen_movement(
                            board, row, col, self.max_pieces)
                        if added_legals:
                            for i in added_legals:
                                legals.append(
                                    f"{self.max_alph[col]}{row}{self.max_alph[i[1]]}{i[0]}")
        return legals
