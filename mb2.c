#include <stdio.h>

void meow(int n);// prototype to tell compiler that the meow(int n) is coming up in full soon

int main (void)
{
 meow(4);
}

void meow(int n)
{
for (int i =0; i<n; i++)
{
    printf("meow\n");
}


}
