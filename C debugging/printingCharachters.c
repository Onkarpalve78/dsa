#include <stdio.h>
#include <string.h>

int main()
{
    // Strings in C are arrays of characters, terminated by a null character (\0).
    char name[] = "Taher";

    // for(int i=0,i<strlen(name),i++)
    for (int i = 0; i < strlen(name); i++)
    {
        // printf(nums[i]); you didn't use format specifier for char
        printf("%c", name[i]);
        printf("\n");
        printf("%s \n", name);
        printf("integer value: %i \n", i);
        printf("decimal value: %d \n", i);
    }

    return 0;
}