#include <stdio.h>
int A[100];
int size;

void Add(int i)
{
    A[size] = i;
    size++;
}

void Remove()
{
    --size;
}

int Size()
{
    return size;
}

int main(int argc, char **argv)
{
    size = 0;
    for (int i = 0; i < 7; i++)
    {
        Add(i);
        printf("adder \n");
    }
    for (int i = 0; i < Size(); i++)
    {
        Remove();
        printf("remover \n");
    }
}