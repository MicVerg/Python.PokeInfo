def convert(text):
    text.replace(":)", "A").replace(":(","B")

def main():
    text=input()
    convert(text)
    print(text)

main()