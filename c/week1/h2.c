#include <cs50.h>
#include <stdio.h>

int main (void)

{
    string name = get_string ("what is your name?\n");
    int age = get_int ("what is your age\n");
    string phone = get_string ("what is your phone number?\n");
printf("name: %s,\nage: %i,\nphone: %s.\n", name, age, phone);
}
