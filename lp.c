#include <cs50.h>
#include <stdio.h>
void print_row(int length);
int main (void)
{
int h = get_int("what is the height?");
print_row(h);
}
 void print_row(int length)//function of print has an input of length that takes int as a input and it returns nothing because of void just performs the print
{
for (int i=0; i<length;i++)

{
    printf("#");
}


}
