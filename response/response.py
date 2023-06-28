import re
import sys
import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    validators.email(s)
    


if __name__ == "__main__":
    main()