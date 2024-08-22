#include <cs50.h>
#include <stdio.h>

int add_two(int a, int b);
int main (void)

{
    int a = get_int("a: ");
    int b = get_int("b: ");

    int result= add_two (a,b);

    printf("a+b=%i\n", result);

}

int add_two(int a, int b)
{
    return a + b;
}
