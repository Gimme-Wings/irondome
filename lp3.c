#include <stdio.h>
#include <cs50.h>

int main (void)


{int h = get_int("height:");
int l = h;
for (int i = 0; i < l; i++)
{
    for (int j = 0; j <= i; j++)
    {
        printf("#");
    }
    printf("\n");
}
}
