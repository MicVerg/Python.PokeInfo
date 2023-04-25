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
            return 0;
        }
        else if (onlydigits == false)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    //rotate
    int intkey = atoi(argv[1]);
    string plaintext = get_string("plaintext: ");




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
    char result;
    if (isupper(c))
    {
        subtracted = c - 65;
        addkey = (subtracted + n) % 26;
        result = char(addkey);
    }
    else if (islower(c))
    {
        subtracted = c - 97;
        addkey = (subtracted + n) % 26;
        result = char()(addkey);
    }
    return result;
}
