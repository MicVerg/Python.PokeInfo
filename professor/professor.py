import random


def main():
    ...


def get_level():
    # prompt for a level and reprompt if needed
    level = input("Level: ")
    level = int(level)
    while True:
        if not level == 1 or level == 2 or level == 3:
            level = input("Level: ")
            level = int(level)


def generate_integer(level):
    # return a non-negative integer with LEVEL digits or raise a ValueError if level is not 1 2 or 3


if __name__ == "__main__":
    main()