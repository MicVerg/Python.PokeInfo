def main():
    text=input()
    convert(text)
    print(text)


def convert(text):
    text = text.replace(":)", "A").replace(":(","B")
    return text

main()