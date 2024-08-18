#include <stdio.h>
#include <cs50.h>

int main (void)
{int change,coins; coins=0;
do
{
change = get_int("how much change?");
} while(change<0);
while (change>0)
{
    if(change>=25)
{change= change-25;
coins++;
}
    else if (change >=10)
    {
        change= change-10;
        coins++;
    }

else if(change>=5)
{
    change=change-5;
    coins++;
}
if (change>0)
{
    change=change-1;
    coins++;
}

}printf("%i",coins);
}
