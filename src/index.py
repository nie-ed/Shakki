import random
import time
from board import Board
from moves import Moves
        

def main():
    """function that communicated with the AI platform
    """
    board = Board()
    moves = Moves()


    while True:
        opponent_move = input()
        time.sleep(random.randrange(1,10)/100)

        if opponent_move.startswith("RESET:"):
            print("Board reset!")

        elif opponent_move.startswith("PLAY:"):
            choice = moves.make_move(board.board)
            board.update_board(choice, moves.alph)
            # example about logs
            print(f"I chose {choice}!")
            # example about posting a move
            print(f"MOVE:{choice}")

        elif opponent_move.startswith("MOVE:"):
            move = opponent_move.removeprefix("MOVE:")
            print(f"Received move: {move}")
            board.update_board(move, moves.alph)
        else:
            print(f"Unknown tag: {opponent_move}")
            break

if __name__ == "__main__":
    main()
