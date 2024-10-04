#include <stdio.h>

int size = 10;
int main()
{
    int a = 4;
    int b = a;
    int c = a--;
    size = 8;
    printf("%d \n", size);
    printf("b:%d, c:%d, a:%d", b, c, a);
    return 0;
}