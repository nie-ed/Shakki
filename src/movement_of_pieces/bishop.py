class Bishop:
    """Class, which checks the legal moves of a bishop piece, and adds them to a list.
        
    """
    def __init__(self):

        pass
    
    def bishop_movement(self, board, row, col, legals, opponent_pieces, alph):
        """Checks if a move to a specific part of the board is okay to do.

        Args:
            board (Board): Board and its state in a list of lists form.
            row (int): Integer value of row on board.
            col (int): Integer value of colum on board.
            legals (list): List of legal moves.
            opponent_pieces (list): List of opponents pieces in str form. 
            alph (list): List of the alpabetic characters of columns on the board.
        """
        #if bishop next to the right wall
        if col ==7:
            # if bishop next to the right wall and next to the upper wall
            if row == 1:
                for index in range(1, (8-col)):
                for index, index in enumerate(range(col, 1, -1)):
                    if board[row+index][index-col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                    elif board[row+index][index-col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                        break
                    else:
                        break

            # if bishop next to the right wall, on row 2-6
            if row >= 2 and row <=7:
                for index, index in enumerate(range(col, 1, -1)):
                    if board[row+index][index-col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                    elif board[row-index][index-col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                    elif board[row+index][index-col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                        break
                    elif board[row-index][index-col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                        break
                    else:
                        break

            #if bishop next to the right wall and on the last row, row 8
            if row == 8:
                for index, index in enumerate(range(col, 1, -1)):
                    if board[row-index][index-col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                    elif board[row-index][index-col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                        break
                    else:
                        break


        # if bishop somewhere in the middle, where movement everywhere is possible
        if row >= 2 and row <= 7 and col >= 1 and col <= 6:
            #movement to the left
            for index, index in enumerate (range(col, 1, -1)):
                if board[row+index][index-col] == ".": 
                    legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                elif board[row-index][index-col] == ".": 
                    legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                elif board[row+index][index-col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                    break
                elif board[row-index][index-col] in opponent_pieces: 
                    legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                    break
                else:
                    break

            #movemet to the right
                for index in range(1, (8-col)):
                    if 8-row >= index:
                        if board[row+index][index+col] == ".": 
                            legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                        elif board[row-index][index+col] == ".": 
                            legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                        elif board[row+index][index+col] in opponent_pieces: 
                            legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                            break
                        elif board[row-index][index+col] in opponent_pieces: 
                            legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                            break
                        else:
                            break


        #if row ==8 and somewhere in the middle
        if row ==8:
            if col>=1 and col <=6:
                #movement to the left
                for index, index in enumerate (range(col, 1, -1)):
                    if board[row-index][index-col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                    elif board[row-index][index-col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row-index}")
                        break
                    else:
                        break

                #movemet to the right
                for index in range(1, (8-col)):
                    if board[row-index][index+col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                    elif board[row-index][index+col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                        break
                    else:
                        break


        #if row ==1 and somewhere in the middle
        if row ==1:
            if col>=1 and col <=6:
                #movement to the left
                for index, index in enumerate (range(col, 1, -1)):
                    if board[row+index][index-col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                    elif board[row+index][index-col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index-col]}{row+index}")
                        break
                    else:
                        break

                #movemet to the right
                for index in range(1, (8-col)):
                    if board[row+index][index+col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                    elif board[row+index][index+col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                        break
                    else:
                        break


        #if bishop next to the left wall
        if col ==0:
            # if bishop next to the left wall and next to the upper wall
            if row == 1:
                for index in range(1, (8-col)):
                    if board[row+index][index+col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                    elif board[row+index][index+col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                        break
                    else:
                        break

            # if bishop next to the left wall, on row 2-6
            if row >= 2 and row <=7:
                for index in range(1, (8-col)):
                    if board[row+index][index+col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                    elif board[row-index][index+col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                    elif board[row+index][index+col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row+index}")
                        break
                    elif board[row-index][index+col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                        break
                    else:
                        break

            #if bishop next to the right wall and on the last row, row 8
            if row == 8:
                for index in range(1, (8-col)):
                    if board[row-index][index+col] == ".": 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                    elif board[row-index][index+col] in opponent_pieces: 
                        legals.append(f"{alph[col]}{row}{alph[index+col]}{row-index}")
                        break
                    else:
                        break




#TO DO:
# next to the left wall and the middle
# next to the left wall and the upper wall
# next tot the left wall and the bottom wall