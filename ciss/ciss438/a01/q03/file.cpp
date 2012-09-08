#include <iostream>

#include "Person.h"
#include "Dungeon.h"
#include "Constants.h"

int main()
{
	Person person;
	Dungeon dungeon(5);
	dungeon.join(0, N, 1, S);
	dungeon.join(2, W, 3, E);
	dungeon.join(3, S, 4, W);

	return 0;
}