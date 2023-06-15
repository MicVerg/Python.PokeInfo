grocery_list = {}

while True:
    try:

        user_input = input().lower()

        if user_input in grocery_list:
            grocery_list[user_input] += 1
        else:
            grocery_list[user_input] = 1

    except KeyError:
        pass

# start print UPPERCASE, sorted alpha, starting with value
    except EOFError:
        for item, count in sorted(grocery_list.items()):
            print(count, (item.upper()))
        break