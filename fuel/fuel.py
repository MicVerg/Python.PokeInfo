
while True:
    try:
        user_input = input("Fraction: ")
        split = user_input.split('/')
        x = int(split[0])
        y = int(split[1])

        percentage = (x / y) * 100
        print(percentage + "%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break