import random
from movement_of_pieces.knight import Knight
from movement_of_pieces.pawn import Pawn
from movement_of_pieces.king import King
from movement_of_pieces.rook import Rook
from movement_of_pieces.bishop import Bishop

class Moves:
    """Class, which creates the objects for the piece movement checking and calls the fuctions to check for legal moves.
    """
    def __init__(self):
        self.moves_made_earlier = []
        self.opponent_alph = ["A", "B", "C", "D", "E", "F", "G", "H"]    
        self.opponent_pieces = ["N", "B", "Q", "K", "R", "P"]
        self.alph = ["a", "b", "c", "d", "e", "f", "g", "h"]    

    def make_move(self, board):
        """Calls the method which checks the legal moves of a piece.

        Args:
            board (Board): Board and its state in a list of lists form.

        Returns:
            str: The chocen move to make, in string form and a for the AI platform can understand.
        """
        knight = Knight()
        pawn = Pawn()
        king = King()
        rook = Rook()
        bishop = Bishop()

        legals = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "p":
                    pawn.pawn_movement(board, row, col, legals, self.opponent_pieces, self.alph)
                if board[row][col] == "n":
                    knight.knight_movement(board, row, col, legals, self.opponent_pieces, self.alph)
                if board[row][col] == "k":
                    king.king_movement(board, row, col, legals, self.opponent_pieces, self.alph)
                if board[row][col] == "r":
                    rook.rook_movement(board, row, col, legals, self.opponent_pieces, self.alph)
                if board[row][col] == "b":
                    rook.rook_movement(board, row, col, legals, self.opponent_pieces, self.alph)




        print(legals)

        legals = list(dict.fromkeys(legals))

        #add here all to minimax, to check, which of the legal moves would be best next

        print(legals)

        choice = random.choices(legals)

        self.moves_made_earlier.append(choice[0])
        

        
        return choice[0]