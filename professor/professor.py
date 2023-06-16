import random
import sys

def main():
    get_level()


def get_level():
    # prompt for a level and reprompt if needed
    while True:
        level = input("Level: ")
        if not level == 1 or level == 2 or level == 3:
            level = input("Level: ")
        else:
            return level




def generate_integer(level):
    # return a non-negative integer with LEVEL digits or raise a ValueError if level is not 1 2 or 3
    return SOMEVARIABLE

if __name__ == "__main__":
    main()