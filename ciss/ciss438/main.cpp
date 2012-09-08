#include <iostream>
#include <cstdlib>
#include <ctime>

#include "DiceGame.h"
#include "View.h"
#include "Player.h"

int main()
{
	srand((unsigned int) time(NULL));

	Player aPlayer;
	DiceGame aDiceGame;
	View aView;

	aPlayer.play(aDiceGame);
	aView.update(aDiceGame);

	return 0;
}