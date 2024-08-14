#include <cs50.h>
#include <stdio.h>

int main (void)
{
int x = 4;
int y = 4-x;
while (y>0)
{
    printf("#");
    x++;
}printf("\n");
}
