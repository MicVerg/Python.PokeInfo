#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt
    ccnr = get_long("Credit card nr? ");
    //checksum
    lastdigit = ccnr % 10;

    secondtolastdigit = (ccnr / 10) % 10;
    //american express 15 digits, starts with 34 or 37

    //mastercard 16 digits, starts with 51 52 53 54 55

    //visa 13 or 16 digits, starts with 4

    //modulo 10

    //print result
}