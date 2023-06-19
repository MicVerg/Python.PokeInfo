from cs50 import get_string


greeting = input("Greeting: ").lower().lstrip()



def main():
    ...


def value(greeting):
    if greeting[0:5] == "hello":
        print("$0", end="")
    elif greeting[0:1] == 'h':
        print("$20", end="")
    else:
        print("$100", end="")


if __name__ == "__main__":
    main()