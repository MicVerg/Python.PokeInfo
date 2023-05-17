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
    if cents > 0:
        break

cents = round(cents * 100)

quarters = int(calculate_quarters(cents))
cents = cents - quarters * 0.25

dimes = int(calculate_dimes(cents))
cents = cents - quarters - dimes * 0.10

nickels = int(calculate_nickels(cents))
cents = cents - quarters - dimes - nickels * 0.05

pennies = int(calculate_pennies(cents))
cents = cents - quarters - dimes - nickels - pennies * 0.01

print("quarters: " , quarters , "dimes: " , dimes , "nickels: " , nickels , "pennies: " , pennies)
coins = quarters + dimes + nickels + pennies

print(coins)