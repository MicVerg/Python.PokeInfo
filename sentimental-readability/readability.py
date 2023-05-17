from cs50 import get_string



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


#count total spaces, then +1 = total amount of words
def count_words(text):
    words = 0
    for i in range (len(text)):
        if(text[i].isspace()):
            words += 1
    return words + 1


# sentences end with . ! ?
def count_sentences(text):
    sentences = 0
    for i in range(len(text)):
        if(text[i] == '.' or text[i] == '!' or text[i] == '?'):
            sentences += 1
    return sentences

#prompt for input
text = get_string("Text: ")

lettersTotal = count_letters(text)
#print(lettersTotal)

wordsTotal = count_words(text)
#print(wordsTotal)

sentencesTotal = count_sentences(text)
#print(sentencesTotal)