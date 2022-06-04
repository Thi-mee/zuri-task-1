# This is my python implementation of rock paper scissors
import random

choice = ['R', 'P', 'S']
computer = random.choice(choice)


# Entry point of game
def play_game():
    print("Rock-R  Paper-P  Scissors-S")
    player_input = input("What do you choose: ")

    # validate input
    checkPlayerInput(player_input)

    # expands from shorthand to full name of moves
    player_move = expandMove(player_input)
    computer_move = expandMove(computer)

    print("Player (" + player_move + ") : CPU (" + computer_move + ") ")

    # Function to print result
    displayResult(player_input, computer)


def checkPlayerInput(player_input):
    while player_input != "R" and player_input != "P" and player_input != "S":
        player_input = input("Invalid Input!! Choose again: ")


def expandMove(move):
    if move == 'R':
        expanded_move = "Rock"
    elif move == 'P':
        expanded_move = "Paper"
    else:
        expanded_move = "Scissors"
    return expanded_move


def displayResult(p, c):
    if (p == 'P' and c == 'R') or (p == 'R' and c == 'S') or (p == 'S' and c == 'P'):
        print("You win")
    elif (p == 'R' and c == 'P') or (p == 'S' and c == 'R') or (p == 'P' and c == 'S'):
        print("Computer Wins")
    else:
        print("It's a Tie\n Try again")
        play_game()


play_game()
