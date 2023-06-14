word = input("camelCase : ")

for char in word:
    if char.isupper():
        char.replace(char, char.lower() + "_")
        print(word)