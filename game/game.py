import random
import sys

while True:
    level = input("Level: ")
    if int(level) < 1:
        level = input("Level: ")

    randy = random.randint(1, level)
    guess = input("Guess: ")
        if guess < randy:
            print("Too small!")
            guess = input("Guess: ")
        elif guess > randy:
            print("Too large!")
            guess = input("Guess: ")
        elif guess == randy:
            print("Just right!")
            sys.exit()