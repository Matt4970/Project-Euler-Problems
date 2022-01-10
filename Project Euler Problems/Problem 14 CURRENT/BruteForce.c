#include <stdio.h>

// Brute Force this Problem.
int main (void)
{
    int number = 13;
    int chain_length = 1;

    // The below loops get the chain length.
    while (number > 1)
    {
        if (number % 2 == 0)
        {
            number = number / 2;
            chain_length++;
        }
        else
        {
            number = (3 * number) + 1;
            chain_length++;
        }
    }

    printf("%i\n", chain_length);

}