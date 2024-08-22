#include <cs50.h>
#include <stdio.h>

bool tri (int a, int b, int c);
int main (void)

    {  int a,b,c, value=0;

do
{ a = get_int("a:");
 b = get_int ("b:");
 c = get_int ("c:");

    } while ( a <= 0 ||  b <= 0 || c <=0);

if (value==0)
{
    printf("true\n");
}
else
{
    printf("false\n");
}
return 0;
    }


    bool tri (int a, int b, int c)
{ return (a+b>c) && (a+c>b) && (b+c>a);

value=0
}


