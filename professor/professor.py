import random
import sys

def main():
    level = get_level()
    questions_counter = 0
    mistake_counter = 0
    correct_counter = 0

    while True:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = input(str(x) + " + " + str(y) + " = ")

        if not int(answer) == int((x + y)):
            questions_counter += 1
            mistake_counter += 1
            print("EEE")
            if mistake_counter >= 3:
                print(str(x) + " + " + str(y) + " = " + str((int(x) + int(y))))

        elif int(answer) == int((x + y)):
            questions_counter += 1
            correct_counter += 1

        if questions_counter >= 10:
            print("Score: " + str(correct_counter))
            break



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