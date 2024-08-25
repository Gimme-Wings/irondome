#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int add(string word);
int main (void)
{//get a and b strings
string words[2];
string a = get_string ("Player 1: ");
string b = get_string ("Player 2: ");

    for (int m = 0, n = strlen(a); m < n; m++) {
    a[m] = toupper(a[m]);
    }
    for (int k = 0, l = strlen(b); k < l; k++) {
    b[k] = toupper(b[k]);
}

words[0]=a;
words[1]=b;
int sum1 = add(words[0]);
int sum2 = add(words[1]);

if (sum1>sum2)
{
    printf("player 1 wins\n");
}
else if(sum2> sum1)
{
    printf("player 2 wins\n");
}
else
{
    printf("tie\n");
}

}


int add(string word){
    int sum = 0;
    for (int i = 0; word[i] != '\0'; i++) {
        sum += word[i];
    }
    return sum;
}

