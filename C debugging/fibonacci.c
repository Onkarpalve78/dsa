#include <stdio.h>

int main()
{
    int n;
    scanf("%i", &n);
    int arr[n];

    int length = sizeof(arr) / sizeof(arr[0]);
    arr[0] = 0;
    arr[1] = 1;
    for (int i = 2; i < length; i++)
    {
        arr[i] = arr[i - 1] + arr[i - 2];
    }

    for (int j = 0; j < length; j++)
    {
        printf("%i ", arr[j]);
    }
}