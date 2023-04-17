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
    int amount = 0;
    while (ccnr != 0) {
        ccnr /= 10;
        amount++;
    }
    printf("digits: %i\n", amount);


    //checksum
    int divider = 10;
    while ((amount/2) != 0) {
        int sumsecondtolast = (ccnr / 10) % divider;
        int multiplysecondtolast = sumsecondtolast * 2;
        int sumtotal = sumtotal + multiplysecondtolast;
        divider = divider * 100;
        amount--;
    }
    printf("sumcheck is: %i\n", sumtotal);
    
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