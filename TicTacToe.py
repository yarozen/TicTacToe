from itertools import cycle
import platform
import os
import sys


def init_board():
    return ['#'] + [' '] * 9


def draw_board(b, players, score, game, games):
    if platform.system() == 'Windows':                              # check platform
        os.system('cls')                                            # if Windows - clear screen using 'cls'
    else:
        os.system('clear')                                          # if Linux / os x - clear screen using 'clear'
    print("""
       Tic-Tac-Toe
    Game: {} out of {}
    Score: X:{} - O:{}
    ~~~~~~~~~~~~~~~~~
    {}|{}|{}       7|8|9
    -+-+-       -+-+-
    {}|{}|{}       4|5|6
    -+-+-       -+-+-
    {}|{}|{}       1|2|3
    """.format(game, games,
               score[players[0]], score[players[1]],
               b[7], b[8], b[9],
               b[4], b[5], b[6],
               b[1], b[2], b[3],
               ))


def get_input(board, players, score, game, games):
    while True:
        draw_board(board, players, score, game, games)                  # draw updated board before every turn
        try:
            user_key = int(input("{}'s Turn [1-9]: "
                                 .format(current_player)))              # validate input is integer
            if user_key in range(1, 10):                                # validate input is number between 1-9
                if board[user_key] not in players:                      # validate input is not a position already taken
                    return user_key                                     # if validations pass return key pressed by user
        except ValueError:
            pass


def check_winner(b, p):
    if (
            b[1] == b[2] == b[3] == p or                                # bottom row win
            b[4] == b[5] == b[6] == p or                                # middle row win
            b[7] == b[8] == b[9] == p or                                # upper row win
            b[1] == b[4] == b[7] == p or                                # left column win
            b[2] == b[5] == b[8] == p or                                # middle column win
            b[3] == b[6] == b[9] == p or                                # right column win
            b[1] == b[5] == b[9] == p or                                # upward diagonal win
            b[3] == b[5] == b[7] == p                                   # downward diagonal win
    ):
        return p                                                        # return the winner
    elif ' ' not in board:                                              # if no available spaces declare a tie
        return "Tie"
    return False


def overall_winner(score, players):
    if score[players[0]] == score[players[1]]:
        print("\nIt's a tie!")
    else:
        print("\n{} is the overall winner!".format(max(score, key=score.get)))


games = 5                                                               # set number of games
players = ['X', 'O']                                                    # set players symbol
score = {players[0]: 0, players[1]: 0}                                  # set initial score to 0:0
try:
    for game in range(1, games+1):
        board = init_board()
        player = cycle(range(len(players)))
        if game % 2 == 0:
            current_player = players[next(player)]                      # alternate starting player each game
        winner = False
        while winner is False:
            current_player = players[next(player)]                      # alternate player every turn
            position = get_input(board, players, score, game, games)    # get position from player
            board[position] = current_player                            # mark player position on board
            winner = check_winner(board, current_player)                # check for winner
        if winner != "Tie":
            score[winner] += 1                                          # if it's not a tie raise winner's score
        draw_board(board, players, score, game, games)                  # draw final board
        input("This winner of game {} is: {}. "
              "Press any key to continue...".format(game, winner))      # declare winner of game
    overall_winner(score, players)                                      # show overall winner
except KeyboardInterrupt:
    overall_winner(score, players)
    sys.exit(0)                                                         # show overall winner if user press 'Ctrl-C'
