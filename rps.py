'''
@Author: Stelios Miskedakis - @Realstmiskedakis / @AcidShellgr
Language: Python 3.10.5
Version: 1.0
About Project:
    This is a simple rps game by Stelios Miskedakis

'''

# Packages / Libraries
import os
import random

# It's a list of possible answers for the user.
user_positive = ['yes', 'y']
user_negative = ['no', 'n']

# It's a list of possible actions that the user can choose.
game_actions = ['rock', 'paper', 'scissors']


# The RPS Function
def rps():
    # Points
    user_points = 0
    com_points = 0

    # Starts the game
    #os.system('clear')  # Linux
    os.system('cls')

    try:
        # It's a while loop that runs until the user or the computer reach 3 points.
        while True:
            user = input(">> Choose one of these, ( Rock, Paper and Scissors ): ").lower()
            computer = random.choice(game_actions)  # Computer selects an action

            if user in game_actions and user == computer:
                print("It's a Tie. No One Wins")

            elif user in game_actions and user == 'rock' and computer == 'paper':
                com_points += 1
                print(f"Computer wins, Paper covers rock. Computer Points: {com_points}")

            elif user in game_actions and user == 'rock' and computer == 'scissors':
                user_points += 1
                print(f"You win, Rock Smashes scissors. User Points: {user_points}")

            elif user in game_actions and user == 'paper' and computer == 'rock':
                user_points += 1
                print(f"You win, Paper covers rock. User Points: {user_points}")

            elif user in game_actions and user == 'paper' and computer == 'scissors':
                com_points += 1
                print(f"Computer wins, Scissors cuts paper. Computer Points: {com_points}")

            elif user in game_actions and user == 'scissors' and computer == 'rock':
                com_points += 1
                print(f"Computer wins, Rock smashes scissors. Computer Points: {com_points}")

            elif user in game_actions and user == 'scissors' and computer == 'paper':
                user_points += 1
                print(f"You win, Scissors cuts paper. User Points: {user_points}")

            else:
                print("Invalid Input, Rerun the program.")
                break

            if user_points == 3:
                print("Hooray!! You Win! You reach 3 points!")
                quit()

            elif com_points == 3:
                print("Computer wins... Try again...")
                quit()


    # It's a try and except statement. It's used to catch errors.
    except (TypeError):
        print("Invalid Input, rerun the program.")
        run = False


rps()
