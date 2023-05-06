#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float floatRed = image[i][j].rgbtRed;
            float floatBlue = image[i][j].rgbtBlue;
            float floatGreen = image[i][j].rgbtGreen;
            //calculate average of the 3 pixels
            average = round((floatRed + floatGreen + floatBlue) / 3.0);
            //average = round(average);

            //set each pixel value to that calculated average
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed;
    int sepiaGreen;
    int sepiaBlue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float originalRed = image[i][j].rgbtRed;
            float originalBlue = image[i][j].rgbtBlue;
            float originalGreen = image[i][j].rgbtGreen;
            //calculate sepia values with formula (and round that value to nearest int)
            sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            //if more than 255, cap at 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            //set pixel values to sepia values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //swap horizontally, not vertically

    //make temp x variable
    RGBTRIPLE x;
    int halfWidth = width / 2;
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < halfWidth; j++)
            {
                //swap
                x = image[i][j];
                image[i][j] = image[i][width - 1 - j];
                image[i][width - 1 - j] = x;
            }
        }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //sorry this looks really hard and 
    return;
}
