user_input = input("Input: ")

for char in user_input:
    user_input = user_input.replace('A', '').replace('a', '').replace('E', '').replace('e', '').replace('I', '').replace('i', '').replace('O', '').replace('o', '').replace('U', '').replace('u', '')
print(user_input)