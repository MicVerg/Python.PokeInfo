#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //ask user height integer
    int height;
    do
    {
        height = get_int("What height do you want the stairs to be? ");
    }
    while (height < 1 && height > 8);

    printf("This is the height: %i\n", height);
    //based on height integer, loop that many times, adding #
}