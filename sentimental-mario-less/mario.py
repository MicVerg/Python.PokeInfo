from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height < 1 or height > 8:
        height = get_int("Height: ")
    else:
        break

#i = 0
for i in range(height):
    print('.')
    for j in range(height - 1):
        print('#')