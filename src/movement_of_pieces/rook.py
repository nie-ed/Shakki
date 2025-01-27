class Rook:
    """Class, which checks the legal moves of a rook piece, and adds them to a list.
        
    """
    def __init__(self):

        pass
    
    def rook_movement(self, board, row, col, legals, opponent_pieces, alph):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of colum on board.
            legals (list): List of legal moves.
            opponent_pieces (list): List of opponents pieces in str form. 
            alph (list): List of the alpabetic characters of columns on the board.
        """
        #if rook in col where movement to the right is possible
        if col < 7:
            for i in range(col, 7):
                if board[row][i+1] == ".": 
                    legals.append(f"{alph[col]}{row}{alph[i+1]}{row}")
                elif board[row][i+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[i+1]}{row}")
                    break
                else:
                    break
                
        #if rook in col where movement to the left is possible
        if col > 0:
            for i in range(col, 1, -1):
                if board[row][i-1] == ".": 
                    legals.append(f"{alph[col]}{row}{alph[i-1]}{row}")
                elif board[row][i-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[i-1]}{row}")
                    break
                else:
                    break

        #if rook in row where movement down is possible
        if row < 8:
            for i in range(row, 8):
                if board[i+1][col] == ".": 
                    legals.append(f"{alph[col]}{row}{alph[col]}{i+1}")
                elif board[i+1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{i+1}")
                    break
                else:
                    break

        #if rook in row where movement up ispossible
        if row > 1:
            for i in range(row, 1, -1):
                if board[i-1][col] == ".": 
                    legals.append(f"{alph[col]}{row}{alph[col]}{i-1}")
                elif board[i-1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{i-1}")
                    break
                else:
                    break