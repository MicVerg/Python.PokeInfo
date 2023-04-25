#include <cs50.h>
#include <stdio.h>

int count_letters(string text)
a
int main(void)
{
    //prompt for text
    string text = get_string("Text: ");

    printf("letters: %i\n", letters);
    printf("words: %i\n", words);
    printf("sentences: %i\n", sentences);

    //use formula to calculate grade
    //index = 0.0588 * L - 0.296 * S - 15.8
    //L average number of letters per 100 words - S average number of sentences per 100 words
    //use floats to calc these

}

//write function to count uppercase and lowercase letters
int count_letters(string text)
{
    int letters = 0;
    int strlen = strlen(text);
    int badchars = 0;
    for (int i = 0; i < strlen; i++)
    {
        letters ++;
        if ((word[i]) = " " || "!" || "." || "?")
    }
}

//write function to count words
//count the spaces (spaces + 1 = total words)
int count_words(string text)
{
    int words = 0;
}

//write function to count sentences (sentences end with . ! ?)
int count_sentences(string text)
{
    int sentences = 0;
}