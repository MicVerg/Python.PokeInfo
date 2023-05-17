from cs50 import get_string


def count_letters(text):
    letters = 0
    for i in range(len(text)):
        if (text[i].isalpha()):
            letters += 1
    return letters


# count total spaces, then +1 = total amount of words
def count_words(text):
    words = 0
    for i in range(len(text)):
        if (text[i].isspace()):
            words += 1
    return words + 1


# sentences end with . ! ?
def count_sentences(text):
    sentences = 0
    for i in range(len(text)):
        if (text[i] == '.' or text[i] == '!' or text[i] == '?'):
            sentences += 1
    return sentences


# prompt for input
text = get_string("Text: ")

lettersTotal = count_letters(text)
wordsTotal = count_words(text)
sentencesTotal = count_sentences(text)

# use formula to calculate grade
# index = 0.0588 * L - 0.296 * S - 15.8
# L average number of letters per 100 words - S average number of sentences per 100 words
# use floats to calc these """

grade = 0.0588 * ((lettersTotal / wordsTotal) * 100) - 0.296 * ((sentencesTotal / wordsTotal) * 100) - 15.8

if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print("Grade", round(grade))