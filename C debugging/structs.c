#include <stdio.h>
#include <string.h>

int main()
{
    struct Person
    {
        char name[50];
        int age;
    };

    struct Person person1;
    strcpy(person1.name, "Taher");
    person1.age = 22;

    printf("Name: %s , age: %d", person1.name, person1.age);

    return 0;
}