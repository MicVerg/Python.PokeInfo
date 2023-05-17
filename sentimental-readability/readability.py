from cs50 import get_string

#prompt for input
text = get_string("Text: ")

#//use formula to calculate grade
#//index = 0.0588 * L - 0.296 * S - 15.8
#//L average number of letters per 100 words - S average number of sentences per 100 words
#//use floats to calc these """

def count_letters(text):
    letters = 0
    for i in range(len(text)):
        if(text[i].isalpha()):
            letters += 1
    return letters

lettersTotal = count_letters(text)
print(lettersTotal)