import inflect, sys
from datetime import datetime, date

p = inflect.engine()


def main():
    try:
        year, month, day = input("Date of birth: ").split("-")
    except:
        sys.exit("Invalid date")
    print(calc_minutes(year, month, day))

def calc_minutes(year, month, day):
    user_input_date = date(int(year), int(month), int(day))
    current_date = date.today()

    difference_date = current_date - user_input_date
    difference_date_minutes = difference_date.days * 24 * 60
    difference_in_words = p.number_to_words(difference_date_minutes, andword="")

    return (difference_in_words.capitalize() + " minutes")




if __name__ == "__main__":
    main()