import random
import time
from board import Board
from moves import Moves
        

def main():
    """function that communicated with the AI platform
    """
    board = Board()
    moves = Moves()
    max_alph = ["a", "b", "c", "d", "e", "f", "g", "h"]


    while True:
        opponent_move = input()
        time.sleep(random.randrange(1,10)/100)

        if opponent_move.startswith("RESET:"):
            print("Board reset!")

        elif opponent_move.startswith("PLAY:"):
            choice = moves.make_move(board)
            if not choice:
                print("CHECKMATE")
                break
            board.update_board(choice, max_alph)
            # example about logs
            print(f"I chose {choice}!")
            # example about posting a move
            print(f"MOVE:{choice}")

        elif opponent_move.startswith("MOVE:"):
            move = opponent_move.removeprefix("MOVE:")
            print(f"Received move: {move}")
            board.update_board(move, max_alph)
        else:
            print(f"Unknown tag: {opponent_move}")
            break

if __name__ == "__main__":
    main()
