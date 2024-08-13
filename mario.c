#include <cs50.h>
#include <stdio.h>
int main (void)
{
do
{
    n= get_int("size:")
}   //  int n = get_int("size: ");
 while (n<1);
    // while (n<1)
    // {
     //   n= get_int("size:");
    // }
    for (int i =0; i < n ; i++)
    {
        for (int j = 0; j < n ;j++)
        {
            printf("#");
    }
printf("\n");
}
}

