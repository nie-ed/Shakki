class Knight():
    """Class, which checks the legal moves of a knight piece, and adds them to a list.
        
    """
    
    def __init__(self):
         pass


    def knight_movement(self, board, row, col, legals, opponent_pieces, alph):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of colum on board.
            legals (list): List of legal moves.
            opponent_pieces (list): List of opponents pieces in str form. 
            alph (list): List of the alpabetic characters of columns on the board.
        """
                     
        #if knight somewhere in the center of the board
        if row <= 6 and row >=3:
            #if knight in the middel of the board, movement anywhere whould not hit a wall
            if col >= 2 and col <= 5:
                #knight moves vertically:
                if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")
                if board[row+2][col-1] == "." or board[row+2][col-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-1]}{row+2}")
                if board[row+2][col+1] == "." or board[row+2][col+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+1]}{row+2}")
                
                #knight moves laterally:
                if board[row+1][col+2] == "." or board[row+1][col+2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+2]}{row+1}")
                if board[row+1][col-2] == "." or board[row+1][col-2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-2]}{row+1}")
                if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")
                if board[row-1][col-2] == "." or board[row-1][col-2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-2]}{row-1}")
            
            #if knight is next to the left wall or one col away from the wall, on rows 2-5
            if col ==0 or col==1:
                #knigth moves laterally:
                if board[row+1][col+2] == "." or board[row+1][col+2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+2]}{row+1}")
                if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")
                
                #knight moves vertically:
                if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")
                if board[row+2][col+1] == "." or board[row+2][col+1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col+1]}{row+2}")



            #if knight is next to the right wall or one col away from wall, on rows 2-5
            if col == 7 or col==6:
                #knigth moves laterally:
                if board[row+1][col-2] == "." or board[row+1][col-2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-2]}{row+1}")
                if board[row-1][col-2] == "." or board[row-1][col-2] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-2]}{row-1}")
                
                #knight moves vertically:
                if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                if board[row+2][col-1] == "." or board[row+2][col-1] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[col-1]}{row+2}")
 

#SO FAR OK


        #if knight is at the bottom two rows of the board
        elif row <= 8 and row >=7:
            #if knight is on the 7th row
            if row == 7:
                #if knight is in the middle of the sevent row, can move laterally 2 side an one down
                if col >= 2 or col <=5:
                    if board[row-1][col-2] == "." or board[row-1][col-2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-2]}{row-1}")
                    if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")
                    if board[row+1][col+2] == "." or board[row+1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row+1}")
                    if board[row+1][col-2] == "." or board[row+1][col-2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-2]}{row+1}")
                        
                    #knight can also move 2 up, right or left one
                    if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")
  #SO FAR OKY
                
                #if knigth is on the 7th row, col 1                    
                if col ==1:
                    #knight can move two up, left or right 1
                    if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")  
                    #knight can also move two colums right, one row down or up 
                    if board[row+1][col+2] == "." or board[row+1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row+1}")
                    if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")
                
                #if knight is on the 7th row, col 0           
                if col == 0:
                    #knight can move two colums right one row up or down
                    if board[row+1][col+2] == "." or board[row+1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row+1}")
                    if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")
                    #knight can also move tow rows up, one column right
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}") 
  #SO FAR OKAY
                #if knigth is on the 7th row, col 6                    
                if col ==6:
                    #knight can move two up, left or right 1
                    if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")  
                    #knight can also move two colums right, one row down or up 
                    if board[row+1][col-2] == "." or board[row+1][col-2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-2]}{row+1}")
                    if board[row-1][col-2] == "." or board[row-1][col-2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-2]}{row-1}")
               
                #if knight is on the 7th row, col 7           
                if col == 7:
                    #knight can move two colums right one row up or down
                    if board[row+1][col+2] == "." or board[row+1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row+1}")
                    if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")
                    #knight can also move tow rows up, one column right
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}") 
 
 
            #if knight is on the 8th row                       
            if row == 8:
                #if knight is in the middle of the eight row, can move laterally 2 side an one up
                if col >= 2 or col <=5:
                    if board[row-1][col-2] == "." or board[row-1][col-2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-2]}{row-1}")
                    if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")

                        
                    #knight can also move 2 up, right or left one
                    if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")

                #if knigth is on the 8th row, col 1                    
                if col ==1:
                    #knight can move two up, left or right 1
                    if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")  
                    #knight can also move two colums right, one row down or up 
                    if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")                

                #if knigth is on the 8th row, col 0
                if col == 0:
                    #knight can move two colums right one row down
                    if board[row-1][col+2] == "." or board[row-1][col+2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+2]}{row-1}")
                    #knight can also move tow rows up, one column right
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}") 

                #if knight in 8th row col 6
                if col ==6:
                    #knight can move two up, left or right 1
                    if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}")
                    if board[row-2][col+1] == "." or board[row-2][col+1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col+1]}{row-2}")  
                    #knight can also move two colums right, one up 
                    if board[row-1][col-2] == "." or board[row-1][col-2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-2]}{row-1}")


                #if knight is on the 8th row, col 7           
                if col == 7:
                    #knight can move two colums right one row up or down
                    if board[row-1][col-2] == "." or board[row-1][col-2] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-2]}{row-1}")
                    #knight can also move tow rows up, one column right
                    if board[row-2][col-1] == "." or board[row-2][col-1] in opponent_pieces:
                        legals.append(f"{alph[col]}{row}{alph[col-1]}{row-2}") 
 

    # TO DO:
    #knight movemetn in rows 2, and 1
