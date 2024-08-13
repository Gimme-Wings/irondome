#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char x =get_char("yes or no?");


    if(x=='y' )
    {
        printf("Yes\n");

    }
    else if (x== 'n')
    {
        printf("no\n");
    }
    else
    {printf("not agree\n");
    }
}
