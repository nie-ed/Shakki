def point_evaluation(trial_board): 


    king_dead = True
    for i in trial_board.trial_board:
        if "K" in i:
            king_dead = False
    if king_dead:
        print(f"winning board: {trial_board.trial_board}")
        return 100000
    

    min_pieces = ["N", "B", "Q", "K", "R", "P"]
    max_pieces = ["n", "b", "q", "k", "r", "p"]
    min_piece_val = {"N":3, "B":3, "Q":9, "K":10000, "R":5, "P":1}
    max_piece_val = {"n":3, "b":3, "q":9, "k":10000, "r":5, "p":1}


    #max piece amount by values
    max_piece_amount = 0
    for row in trial_board.trial_board:
        for spot in row:
            if spot in max_pieces:
                max_piece_amount += max_piece_val[spot]
    print(f"max piece amount {max_piece_amount}")

    # min piece amount by values
    min_piece_amount = 0
    for row in trial_board.trial_board:
        for spot in row:
            if spot in min_pieces:
                min_piece_amount += min_piece_val[spot]
    print(f"min piece amount: {min_piece_amount}")


    #if max pawns in the middle, more points for max
    min_pawn_positioning = 0
    max_pawn_positioning = 0
    if trial_board.trial_board[5][3] == "p":
        max_pawn_positioning += 1
        print(f"max pawn position {max_pawn_positioning}")
    if trial_board.trial_board[5][4] == "p":
        max_pawn_positioning += 1

    # if min pawns in the middle, points for min
    if trial_board.trial_board[4][3] == "P":
        min_pawn_positioning += 1
    if trial_board.trial_board[4][4] == "P":
        min_pawn_positioning += 1

    #TODO:
        #- check if king has own or opponent pieces around it
        #- how many legal moves possible?
        #- center occupation, d4, d5, e4, e5
        #- best positioning for different types of pieces


    score = max_piece_amount + max_pawn_positioning - min_piece_amount - min_pawn_positioning
    
    return score
