#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

vector< int > Delta(vector< int >);
void print(vector< int >);

vector< int > Delta(vector< int > x)
{
	sort(x.begin(), x.begin() + x.size());

	vector< int >y;
	for (int j = 1; j < x.size(); j++)
	{
		for (int i = j; i < x.size(); i++)
			y.push_back(x[i] - x[j - 1]);
	}
	sort(y.begin(), y.begin() + y.size());

	return y;
}
void print(vector< int > x)
{
	for (int i = 0; i < x.size(); i++)
		cout << x[i] << ' ';
}
bool operator==(vector< int > x, vector< int > y)
{
	if (x.size() != y.size())
		return false;
	for (int i = 0; i < x.size(); i++)
	{
		if (x[i] != y[i])
			return false;
	}
	return true;
}

string dec2bin(unsigned n)
{
    const int size = sizeof(n) * 8;
    string res;
    bool s = 0;
    for (int a = 0; a < size; a++)
    {
        bool bit = n>>(size - 1);
        if (bit)
            s = 1;
        if (s)
            res.push_back(bit + '0');
        n <<= 1;
    }
    if (!res.size())
        res.push_back('0');
    return res;
}

int main()
{
	string input = "";
	getline(cin, input);

	// Retreive input and put digits into vector
	vector< int >x;
	int i = 0;
	while (input[i] != '-')
	{
		if (input[i] != ' ')
			x.push_back(input[i] - '0');
		i++;
	}

	// Scan from 0 to 2^n (n = size of x)
	for (int i = 0; i < pow(2, x.size()); i++)
	{
		string z = dec2bin(i);
		reverse(z.begin(), z.end());
		for (int j = z.size(); j < x.size(); j++)
			z.push_back('0');
		reverse(z.begin(), z.end());
		
		// Form subset of X using Z and X
		vector< int > y;
		y.push_back(0); // Because there's always a zero
		for (int i = 0; i < z.size(); i++)
		{
			if (z[i] == '1')
				y.push_back(x[i]);
		}
		// If Delta(Y) = Z print Y
		if (Delta(y) == x)
			{ print(y); cout << endl; }
	}

	return 0;
}