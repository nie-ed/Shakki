from minimax.point_evaluation import point_evaluation
from get_legal_moves import get_legal_moves, get_king_legal_moves
from is_king_threatened import is_king_threatened
import copy


class Minimax:
    """Class that contains the minimax algorithim.
    """
    def __init__(self):
        """Class constructor, that initialises variabled needed in minimax.
        """
        self.alph = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.best_move = None
        self.king_row = 0
        self.king_col = 0
        self.max_legal_moves_amount = 0
        self.min_legal_moves_amount= 0

    def minimax(self, current_depth, is_max_turn, board, alpha, beta):
        """Perfoms the minimax algoritmin.

        Args:
            current_depth (int): The currentr depth of the minimax algoritmin.
            is_max_turn (bool): True, if it is maxes turn, if it is mins turn False.
            board (Board): The current Board object.
            alpha (int): The value of alpha for the alpha-beta pruning.
            beta (int): The value of beta for the alpha-beta pruning.

        Returns:
            (int): Score of the current state of the board.
        """



       
        # checks in the current players king is currently threatened
        king_is_threatened = False
        if is_max_turn:
            for row in range(len(board.board)):
                for col in range(len(board.board[row])):
                    if board.board[row][col] == "k":
                        self.king_row = row
                        self.king_col = col
                        king_is_threatened = is_king_threatened(board.board, self.king_row, self.king_col)
                        break
        else:
            for row in range(len(board.board)):
                for col in range(len(board.board[row])):
                    if board.board[row][col] == "K":
                        self.king_row = row
                        self.king_col = col
                        king_is_threatened = is_king_threatened(board.board, self.king_row, self.king_col)
                        break

       
        new_list_of_king_legal_moves = []
        new_list_of_king_legal_moves = get_king_legal_moves(board.board, self.king_row, self.king_col, is_max_turn)

        # find all legal moves for others than the king
        unchecked_new_list_of_legal_moves = []
        unchecked_new_list_of_legal_moves = get_legal_moves(board.board, is_max_turn)



        new_list_of_legal_moves = []
        
        #checks if the move for other than king are going to make king threatened. If so, takes the move away from the legal moves.
        for move in unchecked_new_list_of_legal_moves:
            earlier_board = copy.deepcopy(board.board)
            board.update_board(move, self.alph)                
            does_king_end_up_threatened = is_king_threatened(board.board, self.king_row, self.king_col)
            if does_king_end_up_threatened is False:
                new_list_of_legal_moves.append(move)
            board.board = earlier_board
            earlier_board = None
        

        for i in new_list_of_king_legal_moves:
            new_list_of_legal_moves.append(i)


        if not new_list_of_legal_moves:
            if king_is_threatened:
                #if there are no moves to make and the king is threatened, it is a checkmate
                if is_max_turn:
                    return -10000000
                else:
                    return 10000000
            else:
                # if there are no moves to make but the king is currently, safe it is a draw:
                return 0

        if (current_depth == 0):
            score = point_evaluation(board, self.max_legal_moves_amount, self.min_legal_moves_amount)
            return score

        if is_max_turn:
            self.max_legal_moves_amount = len(new_list_of_legal_moves)
        else:
            self.min_legal_moves_amount = len(new_list_of_legal_moves)

        if (is_max_turn):
            maxi = -1000000
            last_best_move = None
            for move in new_list_of_legal_moves:
                earlier_board = copy.deepcopy(board.board)
                board.update_board(move, self.alph)
                score_now = self.minimax(current_depth - 1, False, board, alpha, beta)
                if max(score_now, maxi) == score_now:
                    maxi = max(score_now, maxi)
                    last_best_move = move
                self.best_move = (last_best_move, maxi)
                board.board = earlier_board
                earlier_board = None
                alpha = max(alpha, maxi)
                if maxi >= beta:
                    break
            return maxi


        else:
            mini = 1000000
            last_best_move = None
            for move in new_list_of_legal_moves:
                earlier_board = copy.deepcopy(board.board)
                board.update_board(move, self.alph) 
                score_now = self.minimax(current_depth - 1, True, board, alpha, beta)
                if min(score_now, mini) == score_now:
                    mini = min(score_now, mini)
                    last_best_move = move
                self.best_move = (last_best_move, mini)
                board.board = earlier_board
                earlier_board = None
                beta = min(beta, mini)
                if mini <= alpha:
                    break
            return mini



        



