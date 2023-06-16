import sys
import inflect

p = inflect.engine()
names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)

    except EOFError:
        names = p.join(names)
        print("Adieu, adieu, to " + names)
        sys.exit()
