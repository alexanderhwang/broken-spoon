#include <string.h>
#include <stdio.h>

int main()
{
	int value1 = 0;
	int value2 = 0;
	int result = 0;
	FILE *file = fopen("Virus", "w");;
	
	printf("\nType in a number: ");
	scanf("%d", &value1);
	printf("\nType in another number: ");
	scanf("%d", &value2);
	result = value1 + value2;
	printf("\nThe sum is %d.\n", result);
	fprintf(file,"%d",result);
	
	return 0;
}
