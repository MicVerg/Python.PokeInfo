def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    for char in word:
        word = word.replace('A', '').replace('a', '').replace('E', '').replace('e', '').replace('I', '').replace('i', '').replace('O', '').replace('o', '').replace('U', '').replace('u', '')
    return word

if __name__ == "__main__":
    main()