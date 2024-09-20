import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess > number:
            print("Too high!")
            
        elif guess < number:
            print("Too low!")

        else:
            print("Congratulations! You guessed the number.")
            break

    except ValueError:
        print("Please enter a valid number")