#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string key);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    string key = argv[1];
    //get input from cl
    //should be one argument in cl
    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        bool onlydigits = only_digits(key);
        if (onlydigits == true)
        {
        //rotate
        int intkey = atoi(argv[1]);
        string plaintext = get_string("plaintext: ");

        int length = strlen(plaintext);
        for (int i = 0; i < length; i++)
        {
            char deciphered = rotate(plaintext[i], intkey);
            printf("ciphertext: %c\n", deciphered);
        }
            return 0;
        }
        else if (onlydigits == false)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    //key is argv[1]
    //prompt user for plaintext

    //move letters by input key, ONLY alphabetical chars tho
    //so change every character to character + key

}
//function that checks if arguments are digits
bool only_digits(string key)
{
    int len = strlen(key);
    for (int i = 0; i < len; i++)
    {
        if (isdigit(key[i]) != 0)
        {
            return true;
        }
    }
    return false;
}

char rotate(char c, int n)
{
    int subtracted = 0;
    int addkey = 0;
    char result = 0;
    if (isalpha(c))
    {
        if (c >= 65 && c <= 90)
        {
            subtracted = c - 65;
            addkey = (subtracted + n) % 26;
            result = addkey+'0';
        }
        else if (c >= 97 && c <= 122)
        {
            subtracted = c - 97;
            addkey = (subtracted + n) % 26;
            result = addkey+'0';
        }
    }
    return result;
}