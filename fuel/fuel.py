
while True:
    try:
        user_input = input("Fraction: ")
        x, blergh, y = user_input.split('/')
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break