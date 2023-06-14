due = 0
paid = 0

while True:
    input = input("Insert Coin: ")
    paid += int(input)
    due = 50 - paid
    print("Amount Due: " + str(due))

    if due <= 0:
        break
