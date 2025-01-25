import random
import time

def set_board(board: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
    print(f"Set board to {board}")
    board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    return board

def make_move(board: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
#    legal_moves = [move.uci() for move in list(board.legal_moves)]
 #   print(f"I found {len(legal_moves)} legal moves: {', '.join(legal_moves)}")
  #  choice = random.choice(legal_moves)
   # board.push_uci(choice)

    return "E6E4"

def main():

    board = "r n b q k b n r /n p p p p p p p p /n . . . . . . . . /n . . . . . . . . /n . . . . . . . . /n . . . . . . . . /n P P P P P P P P /n R N B Q K B N R"
    
    print(board)

    while True:
        opponent_move = input()
        time.sleep(random.randrange(1,10)/100)
        if opponent_move.startswith("PLAY:"):
            choice = make_move(board)
            # example about logs
            print(f"I chose {choice}!")
            # example about posting a move
            print(f"MOVE:{choice}")
            board_now = "rnbqkbnr/pppppppp/8/8/8/P2P4/1PP1PPPP/RNBQKBNR"
            print(f"BOARD:{board_now}")


        elif opponent_move.startswith("MOVE:"):
            move = opponent_move.removeprefix("MOVE:")
            #LAITA TÄHÄN TAPA MUUTTAA MITÄ ON LAUDALLA
            board = "r n b q k b n r /n p p p . p p p p /n . . . p . . . . /n . . . . . . . . /n . . . . . . . . /n . . . . . . . . /n P P P P P P P P /n R N B Q K B N R"
            print(f"Received move: {move}")
            print(move)
        else:
            print(f"Unknown tag: {opponent_move}")
            break

if __name__ == "__main__":
    main()



   #     elif opponent_move.startswith("RESET:"):
    #        board.reset()
     #       print("Board reset!")