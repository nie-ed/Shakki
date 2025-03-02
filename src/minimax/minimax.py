from minimax.point_evaluation import point_evaluation
from get_legal_moves import get_legal_moves, get_king_legal_moves
from is_king_threatened import is_king_threatened
import copy



class Minimax:
    def __init__(self):
        self.alph = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.best_move= None
        self.last_legals = []
        self.king_row = 0
        self.king_col = 0 

    def minimax(self, current_depth, is_max_turn, board, a, b):

       
        print(f"max turn: {is_max_turn}")

        # lets check if the king is threatened currently
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


        #find_all_legal_moves_for_the_king
        
        new_list_of_king_legal_moves = []
        new_list_of_king_legal_moves = get_king_legal_moves(board.board, self.king_row, self.king_col, is_max_turn)
        print(f"king legals {new_list_of_king_legal_moves}")

        #find all legal moves for others than the king
        new_list_of_legal_moves = []
        new_list_of_legal_moves = get_legal_moves(board.board, is_max_turn)


        print(f"threathenes {king_is_threatened}")


        #lets check, which of the legals moves for others than the king, would protect the king
        if king_is_threatened:
            old_legals = new_list_of_legal_moves.copy()
            new_list_of_legal_moves = []
            for move in old_legals:
                earlier_board = copy.deepcopy(board.board)
                board.update_board(move, self.alph)                
                is_king_still_threatened = is_king_threatened(board.board, self.king_row, self.king_col)
                if not is_king_still_threatened:
                    new_list_of_legal_moves.append(move)
                board.board = earlier_board
            #if the king is threatened and there are no moves to make, it is a checkmate, return (-)10000000
            new_list_of_legal_moves.extend(new_list_of_king_legal_moves)

            if not new_list_of_legal_moves:
                if is_max_turn:
                    return -10000000
                else:
                    return 10000000


        else:
            new_list_of_legal_moves.extend(new_list_of_king_legal_moves)
            #if there are no legal moves to make, it is a draw
            if not new_list_of_legal_moves:
                return 0
        


        if (current_depth == 0):
            print(f"legals to go to point eval {new_list_of_legal_moves}")
            score = point_evaluation(board, new_list_of_legal_moves, is_max_turn)
            print(score)
            return score


        if (is_max_turn):
            maxi = -1000000
            last_best_move = None
            for move in new_list_of_legal_moves:
                earlier_board = copy.deepcopy(board.board)
                board.update_board(move, self.alph)
                score_now = self.minimax(current_depth - 1, False, board, a, b)
                if max(score_now, maxi) == score_now:
                    maxi = max(score_now, maxi)
                    last_best_move = move
                self.best_move = (last_best_move, maxi)
                board.board = earlier_board
                a = max(a, maxi)
                if maxi >= b:
                    break
            return maxi


        else:
            mini = 1000000
            last_best_move = None
            for move in new_list_of_legal_moves:
                earlier_board = copy.deepcopy(board.board)
                board.update_board(move, self.alph) 
                score_now = self.minimax(current_depth - 1, True, board, a, b)
                if min(score_now, mini) == score_now:
                    mini = min(score_now, mini)
                    last_best_move = move
                self.best_move = (last_best_move, mini)
                board.board = earlier_board
                b = min(b, mini)
                if mini <= a:
                    break
            return mini



        



