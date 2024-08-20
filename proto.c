#include <cs50.h>
#include <stdio.h>
void print_column( height)
int i, h, height;
int main (void)

{
    h =get_int("height:");
    print_column (h)
}

void print_column( height )
{
 for ( i = 0; i < height; i++)
{
    printf("#\n");
}
}
