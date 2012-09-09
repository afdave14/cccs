#ifndef VIEW_H
#define VIEW_H

#include "DiceGame.h"

class View {
public:
	void update(DiceGame dicegame) const
	{
		int fv1 = dicegame.get_d1_face_value();
		int fv2 = dicegame.get_d2_face_value();
		int sum = fv1 + fv2;

		std::cout << "Dice  : " << fv1 << ", " << fv2 << std::endl;
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