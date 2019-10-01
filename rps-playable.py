import random
import time

moves = ['rock', 'paper', 'scissors']

def move():
    return random.choice(moves)

def play_game():
    while True:
        playGame = input("Would you like to play a game of rock, paper or scissors? Yes or No").lower()
        if "yes" in playGame:
            new_game()
        elif "no" in playGame:
            print("Goodbye")
            break
        else:
            print("sorry I don't understand")

def play_again():
    while True:
        play_again = input("would you like to play again? yes or No").lower()
        if "yes" in play_again:
            new_game()
        elif "no" in play_again:
            print("goodbye")
            break
        else:
            print("Sorry, I don't understand. Please try again")

def rounds_won():
    rounds = 0
    rounds += 1
    print(rounds)

def draw():
    print("You drew")

def win():
    print("you won")

def lose():
    print("you lost")

def new_game():
    playerMoves = []
    computerMoves = []
    y_score = 0
    c_score = 0
    for round in range(3):
        ym = input('Your move: Rock, Paper or Scissors?').lower()
        if ym in moves:
            playerMoves.append(ym)
            print(f'You chose {ym}')
            cm = move()
            computerMoves.append(cm)
            print(f'Computer chose {cm}')
            print(playerMoves)
            print(computerMoves)
            if ym == cm:
                draw()
            elif ym == 'rock' and cm == 'scissors' or ym == 'scissors' and cm == 'paper' or ym == 'paper' and cm == 'rock':
                win()
                y_score += 1
                print(y_score)
                print(c_score)
                rounds_won()
            else:
                lose()
                c_score += 1
                print(y_score)
                print(c_score)
        else:
            print("That is not a valid choice. Please try again")
    if y_score > c_score:
        print("You won the game!")
    else:
        print("Sorry, you lost the game")
    rounds_won()
    play_again()

play_game()
# def win_lose():
#     if ym == cm:
#         draw()
#     elif

# def beats():
#     return ((ym == 'rock' and cm == 'scissors') or
#             (ym == 'scissors' and cm == 'paper') or
#             (ym == 'paper' and cm == 'rock'))
