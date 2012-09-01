#include <stdio.h>

/* create direct address lookup lookup_table*/
#define TABLE_SIZE 200000
static unsigned short lookup_table[TABLE_SIZE];

unsigned short CycleLen(unsigned long n)
{
	/* if cycle length for n is in the lookup_table return cycle length */
	if(n < TABLE_SIZE && lookup_table[n]) return lookup_table[n];
	/* check if n is odd (i.e. if n is odd the first bit will be set to one other wise it will be even) */
	else if(n & 1) {
		if(n < TABLE_SIZE) {
			/* since 3n+1 is even(b/c n is odd) perform 3n+1 and a bit shift to the right by 1 to simulate division by 2 */
			lookup_table[n] = 2 + CycleLen((3*n+1) >> 1); 
			return lookup_table[n];
		}
		
		return 2 + CycleLen((3*n+1) >> 1);
	}
	else {
		if(n < TABLE_SIZE) {
			lookup_table[n] = 1 + CycleLen(n >> 1); 
			return lookup_table[n];
		}
		
		return 1 + CycleLen(n >> 1);
	}
}

int main()
{
	unsigned long input1, input2, num1, num2, i;
	unsigned int output = 0, temp;

	lookup_table[1] = 1;

	while(scanf("%lu %lu", &input1, &input2) != EOF)
	{
		/* added this after original wasnt accepted by the judge */
		if(input1 < input2) {
			num1 = input1;
			num2 = input2;
		}
		else {
			num1 = input2;
			num2 = input1;
		}

		for(i = num2; i >= num1; --i)
		{
			temp = CycleLen(i);
			if(temp > output)
				output = temp;
		}
		
		printf("%lu %lu %hd\n", input1, input2, output);
		output = 0;
	}
	return 0;
}