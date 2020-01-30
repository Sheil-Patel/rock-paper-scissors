
import random
OPTIONS = ["rock", "paper", "scissors"]
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "nobody won"
    elif user_choice == "rock" and computer_choice == "paper":
        return "paper"
    elif user_choice == "paper" and computer_choice == "rock":
        return "paper"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "scissors"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "scissors"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "rock"
    elif user_choice == "scissors" and computer_choice == "rock":
        return "rock"
hello = False

while hello != True:
    print("-------------------")
    print("WELCOME TO MY ROCK-PAPER-SCISSORS GAME!!")
    print("-------------------")

    print("-------------------")
    print("PLEASE SELECT ONE OF THE FOLLOWING OPTIONS:", OPTIONS)

    print("-------------------")
    user_choice = input()
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Sorry you chose and invalid input")
        hello = False
    else:
        hello = True

print(f"YOU CHOSE: '{user_choice}'")
computer_choice = random.choice(OPTIONS)
print(f"COMPUTER CHOSE: '{computer_choice}'")
winning_choice = determine_winner(user_choice, computer_choice)
print(f"WINNING CHOICE: '{winning_choice}'")
print("-------------------")
print("THANKS, PLEASE PLAY AGAIN!")
print("-------------------")
#breakpoint()
#print(dir(random))
#print(help(random.choice)) # then press "q" to quit
#print(type(options))
#print(type(user_choice))


    