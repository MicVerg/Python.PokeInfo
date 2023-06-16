import random
import sys

def main():
    level = get_level()
    mistake_counter = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = input(str(x) + " + " + str(y) + " = ")
        if not answer == (x + y):
            mistake_counter += 1
            print("EEE")

def get_level():
    # prompt for a level and reprompt if needed
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # return a non-negative integer with LEVEL digits or raise a ValueError if level is not 1 2 or 3
    randy = 0
    if level == 1:
        randy = random.randint(1, 9)
    elif level == 2:
        randy = random.randint(10, 99)
    elif level == 3:
        randy = random.randint(100, 999)
    else:
        raise ValueError
    return randy

if __name__ == "__main__":
    main()