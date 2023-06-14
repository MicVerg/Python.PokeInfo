
while True:
    try:
        user_input = input("Fraction: ")
    except ValueError:
        pass
    except ZeroDivisionError:
        pass