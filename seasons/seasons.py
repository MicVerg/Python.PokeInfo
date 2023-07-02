import inflect, re, sys
from datetime import date, datetime

p = inflect.engine()


def main():
    try:
        user_input = input("Date of birth: ")
        user_input_date = datetime.strptime(user_input, "%Y-%m-%d")
        current_date = datetime.now()

        difference_date = current_date - user_input_date
        print(difference_date)
    except 




def calculate():



if __name__ == "__main__":
    main()