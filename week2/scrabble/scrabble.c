#include <cs50.h>
#include <stdio.h>

int main (void)
{//get a and b strings
string words[2];
words[0] = get_string ("Player 1: ");
words[1] = get_string ("Player 2: ");
printf("%i%i\n", words[0][0], words[1][0]);
}
