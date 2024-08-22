#include <cs50.h>
#include <stdio.h>

// Function prototype
float multiply(int a, int b);

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
int multiply(int a, int b)
{
    return a * b;
}
