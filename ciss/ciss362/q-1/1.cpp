#include <iostream>

using namespace std;

bool is_prime(int n)
{
	if (n % 2 == 0)
		return false;
	for (int i = n; i > 2; i--)
	{
		if (n % i == 0)
			return true;
	}
	return true;
}

int main()
{
	int num;
	cin >> num;
	cout << is_prime(num);
	
	return 0;
}