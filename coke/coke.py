due = 0
paid = 0

print("Amount Due: 50")

while True:
    user_input = input("Insert Coin: ")
    paid += int(user_input)
    due = 50 - paid
    print("Amount Due: " + str(due))

    if due <= 0:
        break
