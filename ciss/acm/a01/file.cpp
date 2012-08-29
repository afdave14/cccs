#include <iostream>

using namespace std;

int conj(int x)
{
	x = (x % 2 == 0 ? x / 2 : x * 3 + 1);
	return x;
}

int main()
{
	int x;
	cin >> x;
	
	while (x != 1)
	{
		x = conj(x);
		cout << x << endl;
	}
	return 0;
}