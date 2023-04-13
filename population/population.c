#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startsize;
    do
    {
        startsize = get_int("What's the start population size? ");
    }
    while (startsize < 9);

    // TODO: Prompt for end size
    int endsize;
    do
    {
        endsize = get_int("What's the end population size? ");
    }
    while (endsize < startsize);

    // TODO: Calculate number of years until we reach threshold
    int llamas = 0;
    int years = 0;
    do
    {
        llamas = startsize + (startsize / 3) - (startsize / 4);
        years ++;
    }
    while (llamas < endsize);

    printf("Years: %i\n", years);


    // TODO: Print number of years
}
