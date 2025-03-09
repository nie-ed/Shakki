from movement_of_pieces.knight import Knight
from movement_of_pieces.pawn import Pawn
from movement_of_pieces.king import King
from movement_of_pieces.rook import Rook
from movement_of_pieces.bishop import Bishop
from movement_of_pieces.queen import Queen


def get_king_legal_moves(board, row, col, is_max_turn):
    """Gets the legal moves a king can make.

    Args:
        board (list): The current state of the chess board.
        row (int): The row number the king is located at on the board.
        col (_type_): The col number the king is located at on the board.
        is_max_turn (bool): Tells if it is max players turn.

    Returns:
        list : A list of moves the king can legally make.    
    """

    king = King()
    board_alph = ["a", "b", "c", "d", "e", "f", "g", "h"]

    legals = []

    added_legals = king.king_movement(board, row, col, is_max_turn)
    if added_legals:
        for i in added_legals:
            legals.append(f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

    return legals


def get_legal_moves(board, max_player):
    """Gets the moves the other pieces than king can make. Does not yet check of moves are fully legal.

    Args:
        board (list): The current state of the chess board.
        max_player (bool): Tells if it is max players turn.

    Returns:
        list : A list of the moves that can be make.
    """

    knight = Knight()
    pawn = Pawn()
    rook = Rook()
    bishop = Bishop()
    queen = Queen()
    board_alph = ["a", "b", "c", "d", "e", "f", "g", "h"]
    min_pieces = ["N", "B", "Q", "K", "R", "P"]
    max_pieces = ["n", "b", "q", "k", "r", "p"]

    legals = []

    if max_player:
        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] == "p":
                    added_legals = pawn.pawn_movement(
                        board, row, col, min_pieces, True)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "n":
                    added_legals = knight.knight_movement(
                        board, row, col, max_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "r":
                    added_legals = rook.rook_movement(
                        board, row, col, max_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "b":
                    added_legals = bishop.bishop_movement(
                        board, row, col, max_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "q":
                    added_legals = queen.queen_movement(
                        board, row, col, max_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

    else:
        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] == "P":
                    added_legals = pawn.pawn_movement(
                        board, row, col, max_pieces, False)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "N":
                    added_legals = knight.knight_movement(
                        board, row, col, min_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "R":
                    added_legals = rook.rook_movement(
                        board, row, col, min_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "B":
                    added_legals = bishop.bishop_movement(
                        board, row, col, min_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")

                if board[row][col] == "Q":
                    added_legals = queen.queen_movement(
                        board, row, col, min_pieces)
                    if added_legals:
                        for i in added_legals:
                            legals.append(
                                f"{board_alph[col]}{row}{board_alph[i[1]]}{i[0]}")
    return legals
