#include <cs50.h>
#include <stdio.h>
void qwer ( int height );

int main (void)

{
    int h =get_int("height:");
   qwer (h); // the print_column is a name for prototype thats coming up executing the print column enters below
}

void qwer( int height )//name of after void could be anything
{
 for ( int i = 0; i < height; i++)
{
    printf("#\n");
}
}

