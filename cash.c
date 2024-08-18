#include <stdio.h>
#include <cs50.h>

int main (void)
{int change,coins; coins=0;
do
{
change = get_int("how much change?");
} while(change<0);
if(change>0)
{change= change-25;
coins++;
}


printf("%i",coins);
}
