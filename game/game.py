import random
import sys

level = input("Level: ")
while True:
    if not level.isdigit() or int(level) < 1:
        level = input("Level: ")
    else:
        randy = random.randint(1, int(level))
        break


while True:
    guess = input("Guess: ")
    if not guess.isdigit():
        guess = input("Guess: ")

    guess = int(guess)
    if guess < randy:
        print("Too small!")
    elif guess > randy:
        print("Too large!")
    elif guess == randy:
        print("Just right!")
        sys.exit()
