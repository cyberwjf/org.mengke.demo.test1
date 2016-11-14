#include <stdio.h>
#include <stdlib.h>
#include "insert_sort.h"


void insert_at(int data[], int n)
{
	int temp = data[n];
	for(int i=0;i<n;i++)
	{
		if (data[i] >= temp)
		{
			for(int j=n-1;j>=i;j--)
			{
				data[j + 1] = data[j];
			}
			data[i] = temp;
			break;
		}
	}
}

void insert_sort(int data[], int n)
{
	for(int i=1;i<n;i++)
	{
		insert_at(data, i);
	}
}

