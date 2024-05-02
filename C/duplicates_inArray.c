#include<stdio.h>

int main()
{
	int arr[] = {10,20,30,30,50,20,50,50,10};
	int size = sizeof(arr)/sizeof(arr[0]);

	printf("Duplicate element : ");
	for(int i=0; i<size; i++){
		for(int j=i+1;j<size;j++){
			if (arr[i] == arr[j])
				printf("%d\t",arr[j]);
		}
	}
	printf("\n");
	return 0;
}
