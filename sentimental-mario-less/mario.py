from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height < 1 or height > 8:
        height = get_int("Height: ")
    else:
        break

row = 0
for i in range(row < height):
    for j in range(height - row):
        print('.')
    for k in range()