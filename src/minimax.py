class Minimax:
    def __init__(self):
        self.scores = []
        self.alph = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.last_score = 0

    def minimax(self, get_legal_moves, list_of_legal_moves, current_depth, is_max_turn, target_depth, test_board, self_pieces, opponent_pieces):

        if (current_depth == target_depth):

            opponent_piece_amount = 0
            for i in test_board.test_board:
                if i in opponent_pieces:
                    opponent_piece_amount += 1

            self_pieces_amount = 0
            for i in test_board.test_board:
                if i in self_pieces:
                    self_pieces_amount += 10

            opponent_pawn_position = 0
            self_pawn_position = 0
            for i in range(3, 5):
                if test_board.test_board[i+1][i] or test_board.test_board[i+2][i] in self_pieces:
                    self_pawn_position += 1
                if test_board.test_board[i+1][i] or test_board.test_board[i+2][i] in opponent_pieces:
                    opponent_pawn_position += 1

            score = self_pieces_amount + self_pawn_position - opponent_piece_amount - opponent_pawn_position
            self.scores.append(score)
            return score


        if (is_max_turn):
            for i in list_of_legal_moves:
                test_board.update_board(i, self.alph)
                new_list_of_legal_moves = get_legal_moves(
                    test_board.test_board, False)
                score_now = self.minimax(get_legal_moves, new_list_of_legal_moves, current_depth + 1, 
                                                False, target_depth, test_board, self_pieces, opponent_pieces)
            print(f"scores: {self.scores}")
            if current_depth == 0:
                return self.scores.index(score_now)
            else:
                self.last_score = max(score_now, self.last_score)
                return self.last_score


        else:
            for i in list_of_legal_moves:
                test_board.update_board(i, self.alph)
                new_list_of_legal_moves = get_legal_moves(
                    test_board.test_board, True)

                score_now = self.minimax(get_legal_moves, new_list_of_legal_moves, current_depth + 1,
                             True, target_depth, test_board, self_pieces, opponent_pieces)

            if current_depth == 0:
                return self.scores.index(score_now)
            else:
                self.last_score = min(score_now, self.last_score)
                return self.last_score

