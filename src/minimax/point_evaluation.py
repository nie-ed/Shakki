def point_evaluation(board, max_legal_moves_amount, min_legal_moves_amount): 
    """Calculates a score for the current state of the board.

    Args:
        board (list): Teh current state of the chess board.
        max_legal_moves_amount (int): How many legal moves did max player most recently have to make.
        min_legal_moves_amount (int): How many legal moves did min player most recently have to make.

    Returns:
        int: A integer value for the current state of the board.
    """

    min_pieces = ["N", "B", "Q", "R", "P", "K"]
    max_pieces = ["n", "b", "q", "r", "p", "k"]
    min_piece_val = {"N":30, "B":30, "Q":90, "R":50, "P":10, "K": 1000}
    max_piece_val = {"n":30, "b":30, "q":90, "r":50, "p":10, "k": 1000}


    

    # Amount of pieces and there respective values
    # Also is the king located at the end rows of the board
    max_piece_amount = 0
    min_piece_amount = 0
    max_king_position = 0
    min_king_position = 0
    for row in board.board:
        for spot in row:
            if spot in max_pieces:
                max_piece_amount += max_piece_val[spot]
            if spot in min_pieces:
                min_piece_amount += min_piece_val[spot]
            if row == 1 or row == 2 and spot == "k":
                max_king_position = 10
            if row == 7 or row == 8 and spot == "K":
                min_king_position = 10

                
    # Max palyer center occupation
    min_center_occupation = 0
    max_center_occupation = 0
    if board.board[5][3] in ["N", "B", "Q", "R", "P"]:
        min_center_occupation += 10
    if board.board[5][4] in ["N", "B", "Q", "R", "P"]:
        min_center_occupation += 10
    if board.board[4][3] in ["N", "B", "Q", "R", "P"]:
        min_center_occupation += 10
    if board.board[4][4] in ["N", "B", "Q", "R", "P"]:
        min_center_occupation += 10

    # Mini player center occupation
    if board.board[4][3] in ["n", "b", "q", "r", "p"]:
        max_center_occupation += 10
    if board.board[4][4] in ["n", "b", "q", "r", "p"]:
        max_center_occupation += 10
    if board.board[5][3] in ["n", "b", "q", "r", "p"]:
        max_center_occupation += 10
    if board.board[5][4] in ["n", "b", "q", "r", "p"]:
        max_center_occupation += 10




    #Beneficial location for knight
    min_knight_position = 0
    max_knight_position = 0
    for x in range(3, 7):
        for y in range(2, 6):
            if board.board[x][y] == "N":
                min_knight_position =+ 2
            if board.board[x][y] == "n":
                max_knight_position =+ 2



    #Is the king protected by own pieces
    king_surroundings = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    max_king_protected = 0
    min_king_protected = 0
    for row in range(len(board.board)):
        for col in range(len(board.board[row])):
            if board.board[row][col] == "k":
                for i in king_surroundings:
                    x = row + i[0]
                    y = col + i[1]
                    if 0 < x < 9 and 0 <= y< 8:
                        if board.board[x][y] in ["n", "b", "q", "r", "p"]:
                            max_king_protected +=1
            if board.board[row][col] == "K":
                for i in king_surroundings:
                    x = row + i[0]
                    y = col + i[1]
                    if 0 < x < 9 and 0 <= y< 8:
                        if board.board[x][y] in ["N", "B", "Q", "R", "P"]:
                            min_king_protected +=1
                        


    score = (max_king_position - min_king_position + max_legal_moves_amount - min_legal_moves_amount + max_piece_amount + max_center_occupation 
    - min_piece_amount - min_center_occupation + max_knight_position - min_knight_position + max_king_protected - min_king_protected)

    return score
