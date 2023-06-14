word = input("camelCase : ")

for char in word:
    if char.isupper():
        new_char = char.replace(char, char.lower() + "_")
        word.insert(char, new_char)
print(word)