import sys
import inflect

p = inflect.engine()
names = []

while True:
    try:
        user_input = input("Name: ")
        names = p.join(user_input)
        print(names)

    except EOFError:
        if len(names) == 1:
            print("Adieu, adieu, to " + names)
            sys.exit()
        elif len(names) == 2:
            print("Adieu, adieu, to " + names + ' and ' + names)
            sys.exit()
        elif len(names) > 2:
            print("Adieu, adieu, to " + names)