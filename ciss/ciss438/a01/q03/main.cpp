#include <iostream>

#include "Person.h"
#include "Dungeon.h"
#include "Constants.h"

int main()
{
	Person person;
	Dungeon dungeon;

	dungeon.create_room();
	dungeon.create_room();
	dungeon.create_room();
	dungeon.create_room();

	dungeon.join(0, 1, N, S);
	dungeon.join(1, 2, E, W);
	dungeon.join(2, 3, S, N);
	dungeon.join(3, 1, S, W);

	dungeon.place_person(person, 0);

	char input;
	int next;
	while(1)
	{
		std::cout << ": ";
		std::cin >> input;
		next = input - '0';

		dungeon.move_person(person, next);
	}

	return 0;
}