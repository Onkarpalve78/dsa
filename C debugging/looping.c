#include <stdio.h>

int main()
{
    int count = 10, names;
    int i = count;

    while (i != 0)
    {
        names = count - i;
        printf("The name count is %d", names);
        // printf("/n")
        printf("\n");
        // i--
        i--;
    }
    // earlier you weren't giving return 0
    // return 0 again misses ;
    return 0;
}