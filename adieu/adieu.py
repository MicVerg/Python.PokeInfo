import sys

names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)

    except EOFError:
        if len(sys.argv) == 2:
            print("Adieu, adieu, to " + names[1])