
while True:
    try:
        user_input = input("Fraction: ")
        x, blergh, y = user_input.split('/')
        print(x, y)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break