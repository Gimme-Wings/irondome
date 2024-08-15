#include <stdio.h>
#include <cs50.h>
int row, column;
int main (void)

do
{
    row = get_int("height?\n");
} while (row>8 || row <1);
