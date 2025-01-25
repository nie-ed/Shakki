class Pawn:
    """Class, which checks the legal moves of a pawn piece, and adds them to a list.
        
    """
    def __init__(self):

        pass
    
    def pawn_movement(self, board, row, col, legals, opponent_pieces, alph):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of colum on board.
            legals (list): List of legal moves.
            opponent_pieces (list): List of opponents pieces in str form. 
            alph (list): List of the alpabetic characters of columns on the board.
        """
        if board[row-1][col] == "." and row <= 7: 
            legals.append(f"{alph[col]}{row}{alph[col]}{row-1}")
        if row==7 and board[row-1][col]=="." and board[row-2][col]==".":
            legals.append(f"{alph[col]}{row}{alph[col]}{row-2}")
        if col >= 1:
            if board[row-1][col-1] in opponent_pieces:
                legals.append(f"{alph[col]}{row}{alph[col-1]}{row-1}")
        if col <= 6:
            if board[row-1][col+1] in opponent_pieces:
                legals.append(f"{alph[col]}{row}{alph[col+1]}{row-1}")
                
        #TO DO
        # if col == 7, change piece type