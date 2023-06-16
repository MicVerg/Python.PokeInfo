import random
import sys

def main():
    get_level()


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
    
    return SOMEVARIABLE

if __name__ == "__main__":
    main()