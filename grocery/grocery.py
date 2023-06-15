
while True:
    try:
        grocery_list = {}
        user_input = input()


        if user_input in grocery_list:
            grocery_list[user_input] += 1
        else:
            grocery_list[user_input] = 1


    except KeyError:
        pass

    except EOFError:
        print(grocery_list.items())