class King:
    """Class, which checks the legal moves of a king piece, and adds them to a list.
        
    """
    def __init__(self):
        pass
    
    def king_movement(self, board, row, col, legals, opponent_pieces, alph):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of column on board.
            legals (list): List of legal moves for this state on the board, for the king.
            opponent_pieces (list): List of opponents pieces in string form. 
            alph (list): List of the alpabetic characters of columns on the board.
        """
        
        # king is somewhere in the middle of the board, and can move any direction
        if row >=2 and row <= 7 and col >=1 and col <= 6:
            if board[row-1][col] == "." or board[row-1][col] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col]}{row-1}")
            if board[row+1][col] == "." or board[row+1][col] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col]}{row+1}")
            if board[row][col+1] == "." or board[row][col+1] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col+1]}{row}")
            if board[row][col-1] == "." or board[row][col-1] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col-1]}{row}")
                
        #if king is at the bottom wall, not touching the left or the right wall
        if row == 8 and col >=1 and col <= 6:
            if board[row-1][col] == "." or board[row-1][col] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col]}{row-1}")
            if board[row][col+1] == "." or board[row][col+1] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col+1]}{row}")
            if board[row][col-1] == "." or board[row][col-1] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col-1]}{row}")       
                
        #if king is at the upper wall, not touching the left or the right wall
        if row == 1 and col >=1 and col <= 6:
            if board[row+1][col] == "." or board[row+1][col] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col]}{row+1}")
            if board[row][col+1] == "." or board[row][col+1] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col+1]}{row}")
            if board[row][col-1] == "." or board[row][col-1] in opponent_pieces: 
                legals.append(f"{alph[col]}{row}{alph[col-1]}{row}")             
    
        # if king in next to the left wall of the board
        if col ==0:
            # if king is somewhere in the middle of the rows, col 0, so not touching upper or bottom wall
            if row >=2 or row <= 7:
                if board[row-1][col] == "." or board[row-1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row-1}")
                if board[row+1][col] == "." or board[row+1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row+1}")    
                if board[row][col+1] == "." or board[row][col+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+1]}{row}")
        
            #if king is next to the left wall and the uppre wall
            if row==1:
                if board[row+1][col] == "." or board[row+1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row+1}")    
                if board[row][col+1] == "." or board[row][col+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+1]}{row}")  
        
            #if king next to the left wall and the bottom wall
            if row==8:
                if board[row-1][col] == "." or board[row-1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row-1}")    
                if board[row][col+1] == "." or board[row][col+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+1]}{row}")
             
        #if king is next to the right wall of the board
        if col == 7:
            # if king is somewhere in the middle of the rows, col 7, so not touching upper or bottom wall
            if row >=2 or row <= 7:
                if board[row-1][col] == "." or board[row-1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row-1}")
                if board[row+1][col] == "." or board[row+1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row+1}")    
                if board[row][col-1] == "." or board[row][col-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-1]}{row}")                                
              
            #if king is next to the right wall and the upper wall
            if row==1:
                if board[row+1][col] == "." or board[row+1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row+1}")    
                if board[row][col-1] == "." or board[row][col-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-1]}{row}")  
        
            #if king next to the left wall and the bottom wall
            if row==8:
                if board[row-1][col] == "." or board[row-1][col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col]}{row-1}")    
                if board[row][col-1] == "." or board[row][col-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-1]}{row}")      
                
                
