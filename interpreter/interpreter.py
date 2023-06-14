input = input("Expression: ")
inputSplit = input.split(' ')

x = float(inputSplit[0])
y = inputSplit[1]
z = float(inputSplit[2])

if y == '+':
    result = x + z
if y == '-':
    result = x - z
if y == '*':
    result = x * z
if y == '/':
    result = x / z

print(result)