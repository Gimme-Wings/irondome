#include <stdio.h>
#include <cs50.h>

int main (void)

{
int x = get_int("height:");
int z = get_int("length");
int y = x-z;
while (z>0)
{
printf("#");
z--;
}

}
