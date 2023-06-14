def convert(text):
    text.replace(":)", "A").replace(":(","B")
    print(text)

def main():
    text=input()
    convert(text)
    print(text)

main()