#include <cs50.h>
#include <stdio.h>
#include <math.h>

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
    int amount = 0;
    while (ccnr != 0) {
        ccnr /= 10;
        amount++;
    }
    printf("amount of digits: %i\n", amount);

    //loop checksum


    for (int digits = 0; digits < amount; digits++)
    {
        int multiply = 0;
        int sum1 = 0;
        int exponent = 1;
        int divider = pow(10, exponent);
        int onedigit = (ccnr / divider) % 10;
        multiply = onedigit * 2;
        sum1 += multiply;

        //increment by 2 to get 10 - 1000 - ..
        exponent += 2;
    printf("divider is: %i\n", divider);
    printf("sum is: %i\n", sum1);
    }



    //checksum
/*     int digit;
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
    } */
/*     int divider = 10;
    int sumtotal = 0;
    while ((amount/2) != 0) {
        int secondtolast = (ccnr / divider) % 10;
        int multiplysecondtolast = secondtolast * 2;
        sumtotal = sumtotal + multiplysecondtolast;
        divider = divider * 100;
        amount--; */

    //printf("sum is: %i\n", total);

/*     long lastdigit = ccnr % 10;

    long secondtolastdigit = (ccnr / 10) % 10;
    long thirdtolastdigit = (ccnr / 100) % 10;
    long fourthtolastdigit = (ccnr / 1000) % 10; */


    //american express 15 digits, starts with 34 or 37

    //mastercard 16 digits, starts with 51 52 53 54 55

    //visa 13 or 16 digits, starts with 4

    //modulo 10

    //print result
}