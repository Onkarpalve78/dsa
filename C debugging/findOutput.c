#include <stdio.h>

int main()
{
    int b = 2;
    for (int a = 2; a >= 0; a--)
    {
        if (a == b)
        {
            printf("1");
        }
        else
        {
            printf("0");
        }
    }

    return 0;
}