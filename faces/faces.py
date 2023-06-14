def main():
    text=input()
    convert(text)


def convert(text):
    text.replace(":)", "A").replace(":(","B")
    print(text)


main()