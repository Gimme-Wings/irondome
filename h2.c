#include <cs50.h>
#include <stdio.h>

int main (void)

{
    string name = get_string ("what is your name?\n");
    int age = get_int ("what is your age\n");
    int phone = get_int ("what is your phone number?\n");
printf("Your info is %s, %i, %i", name, age, phone);
}
