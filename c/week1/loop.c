#include <stdio.h>
#include <cs50.h>

int main (void)
{

   int a = get_int ("what is a equal to?");
   while (a<2)
   {
    printf("meow\n");
    a++;
   }
}
