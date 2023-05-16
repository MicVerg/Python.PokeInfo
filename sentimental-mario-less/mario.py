from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height < 1 or height > 8:
        height = get_int("Height: ")
    else:
        break

row = 0
dots = 1
i = 0
while row < height:
    row += 1
    while dots < (height - row):
        print('.')
        dots += 1
    while i <= row:
        print('#')
        i += 1
    break