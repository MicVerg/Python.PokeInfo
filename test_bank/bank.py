from cs50 import get_string


def main():
    greeting = input("Greeting: ").lower().lstrip()
    print(value(greeting))


def value(greeting):
    if greeting[0:5] == "hello":
        return int("0")
    elif greeting[0:1] == 'h':
        return int("20")
    else:
        return int("100")


if __name__ == "__main__":
    main()