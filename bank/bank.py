from cs50 import get_string


greeting = get_string("Greeting: ").lower()

if greeting.startswith("hello") == true:
    print("0$")
elif greeting.startswith("h", 0):
    print("20$")
else:
    print("100$")