import random
import sys

level = input("Level: ")
randy = random.randint(1, int(level))

while True:
    if int(level) < 1:
        level = input("Level: ")
    else:
        guess = int(input("Guess: "))
        if guess < randy:
            print("Too small!")
        elif guess > randy:
            print("Too large!")
        elif guess == randy:
            print("Just right!")
            sys.exit()
