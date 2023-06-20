
while True:
    try:
        fraction = input("Fraction: ")
        split = user_input.split('/')
        x = int(split[0])
        y = int(split[1])
        if x > y:
            user_input = input("Fraction: ")
        if y == 0:
            user_input = input("Fraction: ")

        percentage = int((x / y) * 100)
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(str(percentage) + "%")

    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

def main():
    fraction = input("Fraction: ")


def convert(fraction):
    split = fraction.split('/')
    x = int(split[0])
    y = int(split[1])
    if x > y:
        fraction = input("Fraction: ")
    if y == 0:
        fraction = input("Fraction: ")


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()