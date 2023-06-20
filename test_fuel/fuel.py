

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    split = fraction.split('/')
    x = int(split[0])
    y = int(split[1])
    if x > y:
        fraction = input("Fraction: ")
    if y == 0:
        fraction = input("Fraction: ")
    percentage = int((x / y) * 100)

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()