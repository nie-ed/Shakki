import random
import time
from board import Board
from moves import Moves
        

def main():
    """function that communicated with the AI platform
    """
    board = Board()
    moves = Moves()
    board_alph = ["a", "b", "c", "d", "e", "f", "g", "h"]


    while True:
        for i in range(1, len(board.board)):
            print(board.board[i])
        opponent_move = input()
        time.sleep(random.randrange(1,10)/100)

        if opponent_move.startswith("RESET:"):
            print("Board reset!")

        elif opponent_move.startswith("PLAY:"):
            print("searching for next move")
            choice = moves.make_move(board)
            if choice[0]:
                board.update_board(choice[0], board_alph)
                print(f"I choice {choice}!")
                print(f"MOVE:{choice[0]}")
            else:
                print(f"MOVE:{choice}")

        elif opponent_move.startswith("MOVE:"):
            move = opponent_move.removeprefix("MOVE:")
            print(f"Received move: {move}")
            board.update_board(move, board_alph)
        else:
            print(f"Unknown tag: {opponent_move}")
            break

if __name__ == "__main__":
    main()
