#include <cs50.h>
#include <stdio.h>
#include <string.h>
int main (void)
{
    string phrase= get_string ("enter phrase: ");

for (int i = 0, int length = strlen (phrase); i < length; i++)
{
printf("%c\n",phrase [i]);
}
}

