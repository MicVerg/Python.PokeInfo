from cs50 import get_string


greeting = input("Greeting: ")

if greeting[0:5].lower() == "hello":
    print("$0", end="")
elif greeting[0:1].lower() == 'h':
    print("$20", end="")
else:
    print("$100", end="")