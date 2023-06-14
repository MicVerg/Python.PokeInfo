word = input("camelCase : ")
new word = ""

for char in word:
    if char.isupper():
        new_char = "_" + char.lower()
        new_word += new_char
    else:
        new_word += char

print(new_word)