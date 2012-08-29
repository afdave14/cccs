#include <iostream>
#include "header.h"
#include "header2.h"

int main()
{
	DoublyLinkedListNode node(9);
	std::cout << node << std::endl;

	DoublyLinkedList a;
	std::cout << a << std::endl;

	a.insert_head(3);
	std::cout << a << std::endl;

	a.insert_head(99);
	std::cout << a << std::endl;

	a.insert_head(22);
	std::cout << a << std::endl;

	a.insert_tail(45);
	std::cout << a << std::endl;

	a.insert_tail(20);
	std::cout << a << std::endl;
	
	DoublyLinkedList b(a);
	std::cout << b << std::endl;

	DoublyLinkedList c;
	c = a;
	std::cout << c << std::endl;

	std::cout << a.size() << std::endl;

	a.remove_head();
	std::cout << a << std::endl;

	b.remove_tail();
	std::cout << b << std::endl;

	c.clear();
	std::cout << c << std::endl;

	std::cout << (a == b) << std::endl;

	a.remove(45);
	std::cout << a << std::endl;

	return 0;
}
