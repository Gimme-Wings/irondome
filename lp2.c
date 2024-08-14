#include <stdio.h>
#include <cs50.h>

int main (void)


{int h = get_int("height:");
int l = h;
while (l>0)
{
    printf("#");
    l--;
    printf("\n");
}
}
