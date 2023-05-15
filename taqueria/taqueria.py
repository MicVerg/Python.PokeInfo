import sys

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            #cost = {menu[item]}
            total += menu[item]
            print(f"Total: $", end="")
            roundedTotal = "{:.2f}".format(total)
            print(roundedTotal)

    except EOFError:
        print()
        sys.exit(0)

