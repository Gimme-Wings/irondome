#include <cs50.h>
#include <stdio.h>
void print_column( int height );

int main (void)

{
    int h =get_int("height:");
    qwert (h);// the print_column here is just a name for the prototype thats about to come up by executing the print column it just enters the bottom loop
}

void qwert( int height )
{
 for ( int i = 0; i < height; i++)
{
    printf("#\n");
}
}

