#include <iostream>

using namespace std;

bool in_order(int array[], int length)
{
	for (int i = 0; i < length - 1; i++)
	{
		if (array[i] > array[i + 1])
			return false;
	}
	return true;
}

void print(int array[], int length)
{
	for (int i = 0; i < length; i++)
		cout << array[i];
	cout << endl;
}

int main()
{
	// Get value from user and assign to temp value
	// for the sake of finding length of value
	int n;
	cin >> n;
	int t = n;

	// Find the length of the value
	int length = 1;
	while (t / 10 != 0)
	{
		length++;
		t /= 10;
	}
	int orig_l = length;
	t = n;

	// Assign the value to an array
	int * p = new int[length];
	for (int i = 0; i < length; i++)
	{
		p[i] = t % 10;
		t /= 10;
	}

	// Reverse the numbers in the array - they were
	// put in backwards
	int * x = new int[length];
	for (int i = length - 1, j = 0; i >= 0; i--, j++)
		x[j] = p[i];


	int max = 0;
	int index = 0;
	while (!in_order(x, orig_l))
	{
		//print(x, orig_l);
		//cout << "Length: " << length << endl;
		// Find largest digit and index of the digit
		for (int i = 0; i < length; i++)
		{
			if (x[i] >= max)
			{
				max = x[i];
				index = i;
			}
		}

		// Flip every number up until that point
		int * temp = new int[index + 1];
		for (int i = 0; i <= index; i++)
			temp[i] = x[i];
		for (int i = index, j = 0; j <= index; j++, i--)
			x[j] = temp[i];
		print(x, orig_l);

		// Flip the whole string of numbers
		delete [] temp;
		temp = new int[length];
		for (int i = length - 1, j = 0; i >= 0; i--, j++)
			temp[i] = x[j];
		//print(temp, length);
		for (int i = 0; i < length; i++)
			x[i] = temp[i];
		print(x, orig_l);
		
		// Exclude the greatest number out of the equation by
		// shortening the length of the array
		length--;
		max = 0;
		index = 0;
	}

	return 0;
}