names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)

    except EOFError:
        print("Adieu, adieu, to " + names[0])