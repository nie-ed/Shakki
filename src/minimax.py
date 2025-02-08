import math
import copy

class Minimax:
    def __init__(self):
        self.scores = []
        self.alph_max = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.alph_min = ["A", "B", "C", "D", "E", "F", "G", "H"]


    def minimax(self, get_legal_moves, list_of_legal_moves, current_depth, is_max_turn, target_depth, test_board, self_pieces, opponent_pieces, last_score):
        
        if (current_depth == target_depth):
            return self.point_evaluation(test_board, self_pieces, opponent_pieces)

        if (is_max_turn):
            self.max_turn(get_legal_moves, list_of_legal_moves, current_depth, target_depth, test_board, self_pieces, opponent_pieces, last_score)

        else:
            self.min_turn(get_legal_moves, list_of_legal_moves, current_depth, target_depth, test_board, self_pieces, opponent_pieces, last_score)


    def point_evaluation(self, test_board, self_pieces, opponent_pieces):       

        #self piece amount
        self_pieces_amount = 0
        for row in test_board.test_board:
            for spot in row:
                if spot in self_pieces:
                    self_pieces_amount += 1
        print(f"self piece amount {self_pieces_amount}")

        #if self pawns in the middle, points
        opponent_pawn_position = 0
        self_pawn_position = 0
        if test_board.test_board[5][3] == "p":
            self_pawn_position += 1
            print(test_board.test_board[4][2])
            print(f"self pawn position {self_pawn_position}")
        if test_board.test_board[5][4] == "p":
            self_pawn_position += 1



        # opponent piece amount
        opponent_piece_amount = 0
        for row in test_board.test_board:
            for spot in row:
                if spot in opponent_pieces:
                    opponent_piece_amount += 1
        print(f"opponent piece amount: {opponent_piece_amount}")

        # if opponent pawns in the middle, points for opponent
        if test_board.test_board[4][3] == "P":
            opponent_pawn_position += 1
            print(f"opponent pawn pos {opponent_pawn_position}")
        if test_board.test_board[4][4] == "P":
            opponent_pawn_position += 1
        score = self_pieces_amount + self_pawn_position - opponent_piece_amount - opponent_pawn_position
        
        return score



    def max_turn(self, get_legal_moves, list_of_legal_moves, current_depth, target_depth, test_board, self_pieces, opponent_pieces, last_score):
        maxi = -math.inf
        for i, move in enumerate(list_of_legal_moves):
            print(f"test board now: last move was mins{test_board.test_board}")
            new_test_board = copy.deepcopy(test_board)
            new_test_board.update_board(move, self.alph_max)
            print(f"test board now: new move by max{new_test_board.test_board}")

            new_list_of_legal_moves = get_legal_moves(
                new_test_board.test_board, False)
            
            score_now = self.minimax(get_legal_moves, new_list_of_legal_moves, current_depth + 1, 
                                            False, target_depth, new_test_board, self_pieces, opponent_pieces, last_score)
            real_score = max(score_now, maxi)
            self.scores[i] = real_score
            print(f"score now: {score_now}")
        return real_score
    

    def min_turn(self, get_legal_moves, list_of_legal_moves, current_depth, target_depth, test_board, self_pieces, opponent_pieces, last_score):
        mini = math.inf
        for i, move in enumerate (list_of_legal_moves):
            print(f"test board now: last move was maxes {test_board.test_board}")
            new_test_board = copy.deepcopy(test_board)
            new_test_board.update_board(move, self.alph_min)
            print(f"test board now: new move by min{new_test_board.test_board}")

            new_list_of_legal_moves = get_legal_moves(
                new_test_board.test_board, True)

            score_now = self.minimax(get_legal_moves, new_list_of_legal_moves, current_depth + 1,
                            True, target_depth, new_test_board, self_pieces, opponent_pieces, last_score)
            print(f"score_now: {score_now}")
            real_score= min(score_now, mini)
            self.scores[i] = real_score
        return real_score
