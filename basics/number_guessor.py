import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Number should be greater than 0")
        quit()
else:
    print("Only type a number!")
    quit()

random_num = random.randint(0, top_of_range)

guesses = 0
while True:
    guesses += 1
    guess = input(f"Enter guess between 0 and {top_of_range}: ")
    if guess.isdigit():
        guess = int(guess)
    if guess == random_num:
        print("Hurray you got it!")
        break
    elif guess > random_num:
        print("Try lower")
    else:
        print("Try above")
    continue

print("You got it in", guesses, "guesses")
