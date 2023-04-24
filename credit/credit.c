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
    while (ccnr != 0)
    {
        ccnr /= 10;
        amount++;
    }
    //printf("amount of digits: %i\n", amount);
    printf("Number is: %ld\n", ccnr2);

    //loop checksum
    int exponent = 1;
    int multiply = 0;
    int sum1 = 0;
    int onedigit = 1;
    long long divider = 1;
    for (int digits = 0; digits < amount; digits++)
    {
        divider = pow(10, exponent);
        onedigit = (ccnr2 / divider) % 10;
        multiply = onedigit * 2;
        if (multiply > 9)
        {
            for (digits = 0; multiply > 0; digits++)
            {
                int split = multiply % 10;
                multiply /= 10;
                sum1 = sum1 + split;
                exponent += 2;
                //digits++;
                printf("loopmultiply is: %d\n", multiply);
                printf("loopsplit is: %d\n", split);
                printf("loopsum is: %i\n", sum1);
            }
        }
        else
        {
        printf("onedigit is: %i\n", onedigit);
        printf("multiply is: %i\n", multiply);
        printf("sum is: %i\n", sum1);
        sum1 += multiply;
        printf("sum is: %i\n", sum1);
        //printf("loopsplit is: %d\n", split);

        //increment by 2 to get 10 - 1000 - ..
        exponent += 2;
    /* printf("divider is: %lld\n", divider);
    printf("onedigit is: %i\n", onedigit);
    printf("multiply is: %i\n", multiply);
    printf("exponent is: %i\n", exponent);
    printf("sum is: %i\n", sum1);
    printf("\n"); */
    }
    }

    //loop for sum2
    int exponent2 = 2;
    int multiply2 = 0;
    int sum2 = 0;
    int onedigit2 = 0;
    long long divider2 = 1;

    onedigit2 = ccnr2 % 10;
    sum2 += onedigit2;
    //printf("sum2 is: %i\n", sum2);
    for (int digits2 = 0; digits2 < amount; digits2++)
    {
        divider2 = pow(10, exponent2);
        onedigit2 = (ccnr2 / divider2) % 10;
        sum2 += onedigit2;
        exponent2 += 2;
        //printf("sum2 is: %i\n", sum2);
    }

    int sum3 = sum1 + sum2;
    printf("sum1 is: %i\n", sum1);
    printf("sum2 is: %i\n", sum2);
    printf("sum3 is: %i\n", sum3);
    if ((sum3 % 10) != 0)
    {
        printf("INVALID\n");
    }
    else if (amount == 15)
    {
        long long divider3 = 1;
        divider3 = pow(10, 14);
        int firstdigit = 0;
        firstdigit = (ccnr2 / divider3) % 10;
        int seconddigit = 0;
        long long divider4 = 1;
        divider4 = pow(10, 13);
        seconddigit = (ccnr2 / divider4) % 10;
        if ((firstdigit == 3) && seconddigit == (4 | 7))
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (amount == 13)
    {
        printf("VISA\n");
    }
    else if (amount == 16)
    {
        long long divider3 = 1;
        divider3 = pow(10, 15);
        int firstdigit = 0;
        firstdigit = (ccnr2 / divider3) % 10;
        if (firstdigit == 5)
        {
            printf("MASTERCARD\n");
        }
        if (firstdigit == 4)
        {
            printf("VISA\n");
        }
    }


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