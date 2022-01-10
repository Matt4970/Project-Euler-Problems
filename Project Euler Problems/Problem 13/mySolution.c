// Find the first 10 digits of the sum of all the digits in numbers.txt
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

# define NUMS 100
# define NUM_LENGTH 50

int numbers[NUMS][NUM_LENGTH];
int nums_to_add[NUM_LENGTH];

int main(void)
{
    // Simply opening the file and making sure it was a success
    FILE *file = fopen("numbers.txt", "r");
    if (file == NULL)
    {
        printf("Failed to open file");
        return 1; 
    }

    // Just looping through the whole file and adding the 50 digit numbers to a 2D array
    int index = 0; // This gets reused later since I like the name index
    int number_index = 0;
    while (feof(file) == 0)
    {
        char temp = fgetc(file);
        if (temp == '\n') 
        {
            number_index++;
            index = 0;
            continue;
        }

        numbers[number_index][index] = (int)temp - 48;
        index++;
    }
    fclose(file); // Don't forget to close files

    // This chunk sums all the starting 50 digits into their places
    int sum_length = 50;
    int *sum = calloc(50, sizeof(int));

    for (int i = 0; i < NUM_LENGTH; i++)
    {
        for (int n = 0; n < NUMS; n++)
        {
            sum[i] += numbers[n][i];
        }
    }

    // This chunk of code relocates all of the digits up. If sum[i] = 553 then 550 is moved up and the 3 remains at sum[i]. Rinse and repeat until all digits are <10.
    index = 49;
    while (index >= 0)
    {
        // Move all the numbers up a place until it is only a single digit in each place
        while (sum[index] > 9)
        {
            // If we need more space in the array reallocate that space and then shift everything to the left adjusting the index
            if (index == 0 && sum[index] > 9)
            {
                sum_length++;
                sum = realloc(sum, sum_length * sizeof(int));
                for (int i = sum_length - 1; i > 0; i--) sum[i] = sum[i - 1]; // Mimic append by moving all the digits to the right
                sum[0] = 0; // Whoops this caused some errors by not doing this after moving all the values
                index++;
            }
            sum[index] -= 10;
            sum[index - 1] += 1;
        }

        index--;
    }

    for (int i = 0; i < sum_length; i++) printf("%i", sum[i]); // Printing the whole number granted only the first 10 digits are needed
    printf("\n");

    free(sum); // Give the mem back
    return 0;
}