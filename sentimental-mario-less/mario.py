from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height < 1 or height > 8:
        height = get_int("Height: ")
    else:
        break


for i in range (1, height + 1):
    print((' ') * (int(height) - i) + ('#') * (i))
    i += 1
