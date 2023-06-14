def main():
    text=input()
    convert(text)
    print(text)
    
def convert(text):
    text.replace(":)", "A").replace(":(","B")



main()