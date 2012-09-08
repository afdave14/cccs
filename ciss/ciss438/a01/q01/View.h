#ifndef VIEW_H
#define VIEW_H

#include "DiceGame.h"

class View {
public:
	void update(DiceGame dicegame) {
		std::cout << "Dice  : " << dicegame.die1.value << ", " << dicegame.die2.value << std::endl;
		int sum = dicegame.die1.value + dicegame.die2.value;
		std::cout << "Sum   : " << sum << std::endl;

		std::cout << "Result: ";
		if (sum == 7)
			std::cout << "won";
		else
			std::cout << "lost";
		std::cout << std::endl;
	}
};

#endif