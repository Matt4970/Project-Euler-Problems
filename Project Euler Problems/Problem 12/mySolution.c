#include <stdio.h>
#include <stdbool.h>
#include <math.h>

const int LIMIT = 100; // For testing purposes

// Prototypes
long triangle_number(int current);
int num_factors(long number);
bool is_integer(long number);

// Main
int main (void){

    int current = 1;
    long number;

    while (true)
    {
        number = triangle_number(current);
        if (num_factors(number) > 500) break;
        current++;
    }

    printf("The number with over 500 divisors is %i.", (int)number);
}

// Return the current triangle number
long triangle_number (int current){
    long sum = 0;
    for (long i = 1; i <= current; i++)
    {
        sum += i;
    }
    return sum;
}

// Return true if the number has more than 500 factors 
int num_factors(long number)
{
    int index = 1;
    int count = 0;

    while (index < (int)sqrtf(number))
    {
        if ((int)number % index == 0)
        {
            count += 2;
        }
        
        index++;
    }
    
    if (is_integer(sqrtf(number))) count++;

    printf("%i, %i\n", (int)number, count);

    return count;
}

// Return true if the number is an integer
bool is_integer(long number)
{
    int temp = (int)number;
    return temp == number;
}