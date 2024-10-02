#include <stdio.h>

int giveSums(int a, int b)
{
    return a + b;
}

float giveDivision(int a, int b)
{
    return (float)a / b;
}

void printAandB(int a, int b)
{
    printf("A: %d , B: %d \n", a, b);
}

int main()
{
    int a, b;

    scanf("%i", &a);
    scanf("%i", &b);
    // printf(giveDivision(10,5));
    int *f = &a;
    printf("%d \n", *f);
    printf("Division: %f \n", giveDivision(a, b));
    printf("Sum: %i \n", giveSums(a, b));
    printAandB(a, b);

    return 0;
}