#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    //prompt
    long ccnr;
    long ccnr2;
    do
    {
        ccnr = get_long("Credit card nr? ");
        ccnr2 = ccnr;
    }
    while (ccnr < 1);

    //amount of digits
    int amount = 0;
    while (ccnr != 0) {
        ccnr /= 10;
        amount++;
    }
    printf("amount of digits: %i\n", amount);
    printf("ccnr is: %ld\n", ccnr2);

    //loop checksum
    int exponent = 1;
    int multiply = 0;
    int sum1 = 0;
    int onedigit = 1;
    //double split = 0;
    long long divider = 1;
    for (int digits = 0; digits < amount; digits++)
    {
        divider = pow(10, exponent);
        onedigit = (ccnr2 / divider) % 10;
        multiply = onedigit * 2;
        if (multiply > 9)
        {
            while(multiply > 0)
            {
                int split = multiply % 10;
                multiply /= 10;
                sum1 = sum1 + split;
                exponent += 2;
                printf("split is: %d\n", split);
            }
        }
        else
        {
        sum1 += multiply;

        //increment by 2 to get 10 - 1000 - ..
        exponent += 2;
    printf("divider is: %lld\n", divider);
    printf("onedigit is: %i\n", onedigit);
    printf("multiply is: %i\n", multiply);
    printf("exponent is: %i\n", exponent);
    printf("sum is: %i\n", sum1);
    printf("\n");
    }
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