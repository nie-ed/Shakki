def point_evaluation(board, legals_for_player, is_max_turn): 

    min_pieces = ["N", "B", "Q", "R", "P"]
    max_pieces = ["n", "b", "q", "r", "p"]
    min_piece_val = {"N":30, "B":30, "Q":90, "R":50, "P":10}
    max_piece_val = {"n":30, "b":30, "q":90, "r":50, "p":10}


    #checking how many legal moves are there to make
    legals_amount = 0
    if is_max_turn:
        legals_amount = len(legals_for_player)
    else:
        legals_amount = (-(len(legals_for_player)))
    

    #max piece amount by values
    max_piece_amount = 0
    for row in board.board:
        for spot in row:
            if spot in max_pieces:
                max_piece_amount += max_piece_val[spot]

    # min piece amount by values
    min_piece_amount = 0
    for row in board.board:
        for spot in row:
            if spot in min_pieces:
                min_piece_amount += min_piece_val[spot]
                


    # if max center occupation , points for max
    min_center_occupation = 0
    max_center_occupation = 0
    if board.board[5][3] in max_pieces:
        max_center_occupation += 1
    if board.board[5][4] in max_pieces:
        max_center_occupation += 1
    if board.board[4][3] in max_pieces:
        max_center_occupation += 1
    if board.board[4][4] in max_pieces:
        max_center_occupation += 1

    # if min center occupation , points for min
    if board.board[4][3] in min_pieces:
        min_center_occupation += 1
    if board.board[4][4] in min_pieces:
        min_center_occupation += 1
    if board.board[5][3] in min_pieces:
        min_center_occupation += 1
    if board.board[5][4] in min_pieces:
        min_center_occupation += 1




    #knight in place where movement possible
    min_knight_position = 0
    max_knight_position = 0
    for x in range(3, 7):
        for y in range(2, 6):
            if board.board[x][y] == "N":
                min_knight_position =+ 3
            if board.board[x][y] == "n":
                max_knight_position =+ 3



    #cheking if king is protected by own pieces
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
                        if board.board[x][y] in max_pieces:
                            max_king_protected +=1
            if board.board[row][col] == "K":
                for i in king_surroundings:
                    x = row + i[0]
                    y = col + i[1]
                    if 0 < x < 9 and 0 <= y< 8:
                        if board.board[x][y] in min_pieces:
                            min_king_protected +=1
                        




    #TODO:
        #- best positioning for different types of pieces


    score = max_piece_amount + max_center_occupation - min_piece_amount - min_center_occupation + legals_amount + max_knight_position - min_knight_position + max_king_protected - min_king_protected

    return score
