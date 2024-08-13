#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char x =get_char("yes or no?");


    if(x =='y' || x=='Y' )
    {
        printf("Yes\n");

    }
    else if (x == 'n' || x=='N')
    {
        printf("no\n");
    }
    else if (x =='c')
    {
        printf("not agree\n");
    }
}
