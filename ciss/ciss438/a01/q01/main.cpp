#include <iostream>
#include <cstdlib>
#include <ctime>

#include "DiceGame.h"
#include "View.h"

int main()
{
	srand((unsigned int) time(NULL));

	DiceGame aDiceGame;
	aDiceGame.play();
	View aView;
	aView.update(aDiceGame);

	return 0;
}