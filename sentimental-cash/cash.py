from cs50 import get_float

while True:
    cents = get_float("Change owed: ")
    if cents < 1:
        cents = get_float("Change owed: ")
        if cents > 0:
            break
    else:
        break

def calculate_quarters