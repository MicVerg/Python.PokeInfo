due = 0
paid = 0

print("Amount Due: 50")

while True:
    user_input = input("Insert Coin: ")
    if user_input == "50" or user_input == "25" or user_input == "10" or user_input == "5":
        paid += int(user_input)
        due = 50 - paid
        print("Amount Due: " + str(due))

    else:
        due = 50 - paid
        print("Amount Due: " + str(due))
        continue

    if due <= 0:
        break
