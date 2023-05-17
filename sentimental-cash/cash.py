from cs50 import get_float

def calculate_quarters(cents):
    cents = cents / 25
    return cents


def calculate_dimes(cents):
    cents = cents / 10
    return cents


def calculate_nickels(cents):
    cents = cents / 5
    return cents


def calculate_pennies(cents):
    return cents


while True:
    cents = get_float("Change owed: ")
    if cents < 1:
        cents = get_float("Change owed: ")
        if cents > 0:
            break
    else:
        break

quarters = calculate_quarters(cents)
cents = 