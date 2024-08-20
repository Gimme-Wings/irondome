#include <cs50.h>
#include <stdio.h>
 int main(void)

 { const int N=3;//const ensures that the number doesnt change
    int scores[N];/put in N to avoid floating around numbers
    for (int i=0; i<N;i++)
    {
        scores[i]=get_int("score: ");// do it however many times is i
    }
    printf("Average: %f\n",(scores[1]+scores[2]+scores[3])/(float)N);//put (float) in front of number to turn it into a float
}

