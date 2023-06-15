import emoji

user_input = input("Input: ")
print(f"Output: {emoji.emojize(user_input, language='alias')}")