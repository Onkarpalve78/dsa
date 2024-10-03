#include <stdio.h>
#include <string.h>

// you're always supposed to define functions before you use it or call in the main function
// else you get implicit declaration of function error
int factorial(int n);
int main()
{
    int ans;
    ans = factorial(4);
    printf("%d", ans);

    return 0;
}

int factorial(int n)
{
    if (n == 0)
    {
        return 1;
    }

    int res = factorial(n - 1);

    return res * n;
}