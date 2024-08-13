#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("whats x? ");
    int y = get_int("whats y? ");

    if(x<y)
    {
        printf("x is less than y");

    }
    else if (x>y)
    {
        printf("x is greater than y");
    }
    else
    {printf("equals\n");
    }
}
