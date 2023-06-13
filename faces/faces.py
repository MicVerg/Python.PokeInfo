def convert(text):
    text.replace(":)", "🙂").replace(":(","🙁")
    print(text)

def main():
    text=input()
    convert(text)
    print(text)

main()