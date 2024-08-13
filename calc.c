#include <cs50.h>
#include <stdio.h>
int add (int a, int b);
int main(void)
{
    int x = get_int("x= ");
    int y = get_int("y= ");

   // this can be used on this line int z= add(x, y);
//but i will add z= function as a replacement below inside the parentheseses
printf("%i\n",  add(x, y));  //printf("x+y\n") is to literrally print what is between the quotes so %i is used for integers and the like

}
int add (int a, int b)//the first int in this line is the return value
{
return a+b ;//these a and b are just representations of x and y as seen in the  int z= add(x,y)

}
