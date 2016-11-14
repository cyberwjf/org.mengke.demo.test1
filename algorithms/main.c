#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "insert_sort.h"

int* generate_input(int n);
void print_array(int data[], int);

#define MAX_VALUE 100
#define MAX_ITEMS 100

int main(int n, char *argv[])
{
    int *data = generate_input(MAX_ITEMS);

	printf("Input Array:\n");

    print_array(data, MAX_ITEMS);
    
    insert_sort(data, MAX_ITEMS);

	printf("Output Array:\n");

    print_array(data, MAX_ITEMS);

    free(data);

    return 0;
}

void print_array(int data[], int n)
{
    for(int i=0;i<n;i++)
    {
        printf("%i ", data[i]);
    }
    putchar('\n');
}

int* generate_input(int n)
{
    int *result = (int *)malloc(sizeof(int) * n);

	srand(time(NULL));

    for(int i=0;i<n;i++)
    {
        result[i] = rand() % MAX_VALUE;
    }

    return result;
}

