import sys
import inflect

p = inflect.engine()
names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)
        names = p.join(names)

    except EOFError:
        print("Adieu, adieu, to " + names)
        sys.exit()

        if len(names) == 1:
            print("Adieu, adieu, to " + names)
            sys.exit()
        elif len(names) == 2:
            print("Adieu, adieu, to " + names + ' and ' + names)
            sys.exit()
        elif len(names) > 2:
            print("Adieu, adieu, to " + names)