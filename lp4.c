#include <stdio.h>
#include <cs50.h>
int height, hash,i,space;
int main (void)
{{
do
{
    height = get_int("height?\n");
} while (height>8 || height <1);
}

for (i=0; i<height;i++)
{for (space=0;space<height;space++)
{
    printf("@");
}
for (hash=0;hash<height-2;hash++)
{
    printf("#");
}printf("\n");

}


}
