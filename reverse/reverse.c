#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

const int HEADER_SIZE = 44;
int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Read header
    uint8_t header[HEADER_SIZE];
    fread(header, HEADER_SIZE, 1, input);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) != 0)
    {
        return 1;
    }

    // Open output file for writing
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(header, HEADER_SIZE, 1, output);

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 0;
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    //return the block size of the wav file in bytes

    //calculate block by =
    // number of channels * bytes per sample (bitsPerSample / 8)
    WORD bytesPerSample = header.bitsPerSample[0] + header.bitsPerSample[1] / 8;
    WORD blockTotal = bytesPerSample * 
    return 0;
}