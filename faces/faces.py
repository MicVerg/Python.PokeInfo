def convert(text):
    text.replace(":)", "🙂").replace(":(","🙁")
    return text

def main():
    text=input()
    convert(text)
    print(text)

if __name__ == "__main__":
    main()