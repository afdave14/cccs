#include <stdio.h>

unsigned long func(unsigned long n)
{
	if (n % 2 == 0)
		return n / 2;
	else
		return 3 * n + 1;
}

int main()
{
	unsigned long first, second, num1, num2;

	while (scanf("%lu %lu", &first, &second) != EOF)
	{
		num1 = first;
		num2 = second;
		if (first > second)
		{
			unsigned long t = second;
			second = first;
			first = t;
		}
		int count = 1;
		int max = 0;
		unsigned long i;
		for (i = first; i <= second; i++)
		{
			unsigned long num = i;
			if (num != 1)
			{
				while (num != 1)
				{
					count++;
					num = func(num);
				}
			}
			if (count > max)
				max = count;
			count = 1;
		}
		printf("%lu %lu %d\n", num1, num2, max);
	}

	return 0;
}