#include <cs50.h>
#include <stdio.h>

int main (void)

{
    printf("type y or n to indicate answer");
char a = get_char("do they wear a white shirt? (y/n)");



if(a=y)
{
    printf("maybe they are still normal");
}
else
{
    printf("going OTD");
    return 0;
}
char b = get_char("is it CT?");

if (b=y)
{
    printf("closer to special");
}
else
{
    printf("probably just regular yeshivish");
    return 0;
}
char c = get_char("do they make weird noises?")
if (c=y)
{
    printf("probably a brisker");
}
else
{
    printf("A CHOFETZ CHAIMER");
    return 0;
}

}
