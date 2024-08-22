#include <cs50.h>
#include <stdio.h>

// Function prototype
float multiply(float a, float b);

int main(void)
{
    // Get input from the user
    float a = get_float("a: ");
    float b = get_float("b: ");

    // Call the multiply function and store the result
    float result = multiply(a, b);

    // Print the result
    printf("%f\n", result);
}

// Function definition
float multiply(float a, float b)
{
    return a * b;
}
