*** Settings ***
Library  ../MovesLibrary.py

*** Test Cases ***
Checkmate In 4
    Checkmate 4 Moves
    Minimax Best Score Should Be  1000000

Checkmate In 3
    Checkmate 3 Moves
    Minimax Best Score Should Be  -1000000

Checkmate In 2
    Checkmate 2 Moves
    Minimax Best Score Should Be  -10000000