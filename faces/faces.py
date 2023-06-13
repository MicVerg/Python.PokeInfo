def convert(text):
    text = text.replace(":)", "🙂").replace(":(","🙁")

def main():
    text=input()
    convert(text)
    print(text)

if __name__ == "__main__":
    main()