#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    //get input from cl
    //should be one argument in cl
    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        return 0;
    }

    //check if input is actually numeral, not alphabetical, not negative, nor empty nor multiple arguments
    //remind user with usage: ./caesar key

    //prompt user for plaintext

    //move letters by input key, ONLY alphabetical chars tho
    //so change every character to character + key

}
//function that checks if arguments are digits
bool only_digits(string s)
{
    int len = strlen(s);
    for (int i = 0; i < len; i++)
    {
        
    }
}
