import random

number_of_rolls = 0
while True:
    wanna_play = input("Roll the dice? (y/n): ").lower()
    
    if wanna_play == "n":
        print("Thanks for playing!")
        break

    elif wanna_play == "y":
        number_of_rolls += 1

        dice_rolls = input("How many times do you want to roll? ")
        if dice_rolls.isdigit:
            dice_rolls = int(dice_rolls)

        numbers = []
        for _ in range(dice_rolls):
            num = random.randint(1, 6)
            numbers.append(num)
        
        if len(numbers) == 1:
            print(f"({numbers[0]})")
        else:
            numbers = tuple(numbers)
            print(numbers)
    else:
        print("invalid choice!")
        continue

print(f"You rolled the dice {number_of_rolls} times.")
