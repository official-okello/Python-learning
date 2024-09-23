import random

choices = ("r", "p", "s")

while True:

    pick = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if pick not in choices:
        print("Invalid choice!")

    else:
        comp_guess = random.choice(choices)

        if pick == comp_guess:
            print("Tie")
        elif ((pick == "r" and comp_guess == "s") or (pick == "p" and comp_guess == "r") or (pick == "s" and comp_guess == "p")):
            print("You win!")
        else:
            print("You lose!")

        print(f"Computer chose {comp_guess}")
        play_again = input("Continue? (y/n): ").lower()

        if play_again == "n":
            break    
        else:
            continue
