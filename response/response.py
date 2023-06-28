import re
import sys
import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    if validators.email(s) == False:
        return "Invalid"
    else:
        return "Valid"


if __name__ == "__main__":
    main()