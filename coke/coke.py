due = 0
paid = 0

print("Amount Due: 50")

while True:
    while True:
        user_input = input("Insert Coin: ")
        if user_input == "50" or user_input == "25" or user_input == "10" or user_input == "5":
            break
        paid += int(user_input)
        due = 50 - paid
        print("Amount Due: " + str(due))

        if due <= 0:
            break
