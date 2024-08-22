#include <cs50.h>
#include <stdio.h>

int add_two(int a, int b);
int main (void)

{
    int a = get_int("a: ");
    int b = get_int("b: ");

   float  result= add_two (a,b);

    printf("a+b=%.2f\n", result);

}

int add_two(int a, int b)
{int sum;
sum = a+b;
    return sum;
}
