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
        print("Too small!")
    elif int(guess) > randy or not guess.isdigit():
        print("Too large!")
    elif int(guess) == randy:
        print("Just right!")
        sys.exit()
