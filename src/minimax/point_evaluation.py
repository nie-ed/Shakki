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


    #max piece amount
    max_piece_amount = 0
    for row in trial_board.trial_board:
        for spot in row:
            if spot in max_pieces:
                max_piece_amount += 1
    print(f"max piece amount {max_piece_amount}")

    #if max pawns in the middle, more points for max
    min_pawn_positioning = 0
    max_pawn_positioning = 0
    if trial_board.trial_board[5][3] == "p":
        max_pawn_positioning += 1
        print(f"max pawn position {max_pawn_positioning}")
    if trial_board.trial_board[5][4] == "p":
        max_pawn_positioning += 1



    # min piece amount
    min_piece_amount = 0
    for row in trial_board.trial_board:
        for spot in row:
            if spot in min_pieces:
                min_piece_amount += 1
    print(f"min piece amount: {min_piece_amount}")

    # if min pawns in the middle, points for min
    if trial_board.trial_board[4][3] == "P":
        min_pawn_positioning += 1
    if trial_board.trial_board[4][4] == "P":
        min_pawn_positioning += 1


    score = max_piece_amount + max_pawn_positioning - min_piece_amount - min_pawn_positioning
    
    return score
