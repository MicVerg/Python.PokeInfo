input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
if input == "42":
    print("Yes")
elif input.lower() == "forty-two":
    print("Yes")
elif input.lower() == "forty two":
    print("Yes")
else:
    print("No")