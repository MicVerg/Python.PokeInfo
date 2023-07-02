import inflect, sys
from datetime import datetime, date

p = inflect.engine()


def main():
    try:
        user_input = input("Date of birth: ")
    except:
        sys.exit("Invalid date")
    print(calc_minutes(user_input))

def calc_minutes(user_input):
    user_input_date = date.strptime(user_input, "%Y-%m-%d")
    current_date = date.today()

    difference_date = current_date - user_input_date
    difference_date_minutes = difference_date.days * 24 * 60
    difference_in_words = p.number_to_words(difference_date_minutes, andword="")

    return (difference_in_words.capitalize() + " minutes")




if __name__ == "__main__":
    main()