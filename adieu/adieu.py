import sys

names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)

    except EOFError:
        if len(names) == 1:
            print("Adieu, adieu, to " + names[0])
            sys.exit()
        if len(names) == 2:
            print("Adieu, adieu, to " + names[0] + ' and ' + names[1])
            sys.exit()
        if len(names) > 2:
            print("Adieu, adieu, to " + )