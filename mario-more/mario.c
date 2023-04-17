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
    while (height < 1 || height > 8);

    //loop
    for (int row = 0; row < height; row++)
    {
        for (int dots = 1; dots < (height - row); dots++)
        {
            printf(" ");
        }
        //left hashes
        for (int i = 0; i <= row; i++)
        {
            printf("#");
        }
        printf("  ");
        //right hashes
        for (int i = 0; i <= row; i++)
        {
            printf("#");
        }
        printf("\n");
    }
}