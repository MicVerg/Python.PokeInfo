#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt
    long ccnr;
    do
    {
        ccnr = get_long("Credit card nr? ");
    }
    while (ccnr < 1);

    //amount of digits
/*     int amount = 0;
    while (ccnr != 0) {
        ccnr /= 10;
        amount++;
    }
    printf("digits: %i\n", amount); */


    //checksum
    int digit;
    int total = 0;
    while (ccnr != 0)
    {
        ccnr = ccnr / 10;
        digit = (ccnr % 10) * 2;

        if (digit > 9)
        {
            total = total + (digit / 10) + (digit % 10);
        }
        else
        {
            total = total + digit;
        }
    }
/*     int divider = 10;
    int sumtotal = 0;
    while ((amount/2) != 0) {
        int secondtolast = (ccnr / divider) % 10;
        int multiplysecondtolast = secondtolast * 2;
        sumtotal = sumtotal + multiplysecondtolast;
        divider = divider * 100;
        amount--; */

    printf("sumcheck is: %i\n", total);

    long lastdigit = ccnr % 10;

    long secondtolastdigit = (ccnr / 10) % 10;
    long thirdtolastdigit = (ccnr / 100) % 10;
    long fourthtolastdigit = (ccnr / 1000) % 10;


    //american express 15 digits, starts with 34 or 37

    //mastercard 16 digits, starts with 51 52 53 54 55

    //visa 13 or 16 digits, starts with 4

    //modulo 10

    //print result
}