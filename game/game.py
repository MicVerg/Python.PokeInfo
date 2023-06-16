import random
import sys

level = input("Level: ")
randy = random.randint(1, int(level))

while True:
    if int(level) < 1 or level.isalpha():
        level = input("Level: ")
    else:
        guess = input("Guess: ")
        if int(guess) < randy or not guess.isdigit():
            print("Too small!")
        elif int(guess) > randy or not guess.isdigit():
            print("Too large!")
        elif int(guess) == randy:
            print("Just right!")
            sys.exit()
