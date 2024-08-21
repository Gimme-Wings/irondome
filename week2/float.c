#include <cs50.h>
#include <stdio.h>
float mult (float a, float b);
int main (void)
{float a = get_float("a: \n");
float b = get_float("b: \n");
mult(a,b);
printf("%f\n", mult);
}
float mult (float a, float b);
{
    return a*b;
}
