def convert(text):
    text = text.replace(":)", "🙂").replace(":(","🙁")

def main():
    text=input()
    convert(text)
    print(text)