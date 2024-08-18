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
while(change>0 && change<25)
{
    if (change >0)
    {
        change= change-10;
        coins++;
    }
}
while(change>0 && change<10)

if(change>0)
{
    change=change-5;
    coins++;
}
while(change>0 && change<5)
if (change>0)
{
    change=change-1;
    coins++;
}

}printf("%i",coins);
}
