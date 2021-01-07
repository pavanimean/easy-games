import random

randnumber = random.randint(1,50)

print("Guess a number between 1 - 50")

while True:
    try:
        guess = input()
    except:
        guess = None

    if guess == None:
        print("Take a guess!")
    elif int(guess) > randnumber:
        print("Lower!")
    elif int(guess) < randnumber:
        print("Higher!")
    else:
        print("You guessed right!")
        break
