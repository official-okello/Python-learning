print('Welcome to Okello comp quiz')

playing = input('Do you wanna play?(Y or N)').lower()

if playing != 'y':
    quit()

print("Yeeey! Let's play :)")
score = 0

answer = input("What is CPU? ").lower()
if answer == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("What is GPU? ").lower()
if answer == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("What is RAM? ").lower()
if answer == 'random access memory':
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("What is PSU? ").lower()
if answer == 'power supply unit':
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

print("You got", score, "questions correct.")
print("You scored", (score/4)*100, "%.")