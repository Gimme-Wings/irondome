#include <cs50.h>
#include <stdio.h>
void print_column( int height );

int main (void)

{
    int h =get_int("height:");
    qwert (h); // the print_column is a name for prototype thats coming up executing the print column enters below
}

void print_column( int height )
{
 for ( int i = 0; i < height; i++)
{
    printf("#\n");
}
}

