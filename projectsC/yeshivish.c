#include <cs50.h>
#include <stdio.h>

int main (void)

{
    printf("type y or n to indicate answer\n");
char a = get_char("do they wear a white shirt? (y/n)\n");



if(a=='y')
{
    printf("maybe they are still normal\n");
}
else
{
    printf("going OTD\n");
    return 0;
}
char b = get_char("is it CT?\n");

if (b=='y')
{
    printf("closer to special\n");
}
else
{
    printf("probably just regular yeshivish\n");
    return 0;
}
char c = get_char("do they make weird noises?\n");
if (c=='y')
{
    printf("probably a brisker\n");
}
else
{
    printf("A CHOFETZ CHAIMER\n");
    return 0;
}

}
