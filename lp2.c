#include <stdio.h>
#include <cs50.h>

int main (void)

{
int x = get_int("height:");
int z = x;
while (x>0)
{
    printf("#");
    x--;
}
printf("\n");
while (z>0)
{
printf("#");
z--;
}

}
