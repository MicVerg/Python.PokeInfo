
while True:
    try:
        items = {}
        user_input = input()


        if user_input in items:
            items[user_input] += 1
        else:
            items[user_input] = 1


    except KeyError:
        pass
    except EOFError:
        print(items)