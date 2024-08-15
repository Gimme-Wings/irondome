#include <stdio.h>
#include <cs50.h>
int height, column,i;
int main (void)
{{{
do
{
    height = get_int("height?\n");
} while (height>8 || height <1);
}
{
for (i=0; i<height;i++)
{
    for (column=0;height-column-1;column++)
{
    printf("#");
 }{ printf("@");
 }
 }

{
    printf("\n");
}
}
}
}
