import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

choices = (ROCK, PAPER, SCISSORS)

def user_choice():
    while True:
        pick = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if pick in choices:
            return pick
        else:
            print("Invalid choice!")

def comp_choice():
    pass

def compare_choices(pick, comp_guess):
    if pick == comp_guess:
        print("Tie")
    elif ((pick == ROCK and comp_guess == SCISSORS) or (pick == PAPER and comp_guess == ROCK) or (pick == SCISSORS and comp_guess == PAPER)):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    while True:       
        pick = user_choice()

        comp_guess = random.choice(choices)

        compare_choices(pick, comp_guess)      

        print(f"Computer chose {comp_guess}")
        play_again = input("Continue? (y/n): ").lower()

        if play_again == "n":
            break
        else:
            continue

play_game()
