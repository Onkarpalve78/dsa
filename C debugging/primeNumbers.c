#include <stdio.h>

int isPrime(int n)
{

    // if (n <= 1) u didnt add this 0,1 are not prime numbers
    //     return 0;

    if (n <= 1)
        return 0;
    // for (int i = 0; i < n / 2; i++) you started i with 0, ofc any number will have modulus 0 if they are divided by 0 or 1
    for (int i = 2; i < n / 2; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int n, i = 0;
    int ans[20] = {0};
    printf("Enter N limit range of prime: ");
    scanf("%i", &n);
    while (i < n)
    {
        if (isPrime(i))
        {
            ans[i] = i;
            printf("Prime number:%d \n", i);
        }

        // i++; you forgot to add this causing infinite loop
        i++;
    }
    int length = sizeof(ans) / sizeof(ans[i]);
    for (int i = 0; i < length; i++)
    {
        printf("%d ", ans[i]);
    }
    return 0;
}