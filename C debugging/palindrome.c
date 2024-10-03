#include <stdio.h>
#include <string.h>

int palindrome(char s[])
{

    int i = 0;
    int j = strlen(s) - 1;

    while (s[i] == s[j] && i >= 0 && j < strlen(s))
    {
        if (i == j)
        {
            return 1;
        }
        i++;
        j--;
    }

    return 0;
}

int main()
{

    int ans = palindrome("TAaT");
    printf("%d", ans);

    return 0;
}