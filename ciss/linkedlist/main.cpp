#include <iostream>
#include "header.h"
#include "header2.h"

int main()
{
	LinkedListNode node(12);
	std::cout << node << std::endl;

	LinkedList c;
	std::cout << c << std::endl;

	c.insert_head(5);
	std::cout << c << std::endl;

	c.insert_head(78);
	std::cout << c << std::endl;

	c.insert_head(1);
	std::cout << c << std::endl;

	c.insert_tail(9);
	std::cout << c << std::endl;

	c.insert_tail(22);
	std::cout << c << std::endl;

	LinkedList d(c);
	std::cout << d << std::endl;

	LinkedList e;
	e = d;
	std::cout << e << std::endl;

	e.remove(78);
	std::cout << e << std::endl;

	return 0;
}