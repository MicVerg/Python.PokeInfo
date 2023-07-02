import inflect, re, sys
from datetime import date, datetime, timedelta

p = inflect.engine()


def main():
    try:
        user_input = input("Date of birth: ")
        user_input_date = datetime.strptime(user_input, "%Y-%m-%d")
        current_date = datetime.now()

        difference_date = current_date - user_input_date
        difference_date_minutes = difference_date.total_minutes()
        print(difference_date_minutes)
    except:
        print("Invalid date")







if __name__ == "__main__":
    main()