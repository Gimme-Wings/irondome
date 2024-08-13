#include <cs50.h>
#include <stdio.h>
int add (int a, int b);
int main(void)
{
    int x =get_int("x; ");
    int y = get_int("y; ");

    int z= add(x, y);

printf("%i\n", z);  //printf("x+y\n") is to literrally print what is between the quotes so %i is used for integers and the like



}
int add (int a, int b)//the first int in this line is the return value
{
return a+b ;

}
