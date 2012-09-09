#ifndef PLAYER_H
#define PLAYER_H


class Player 
{
public:
	void play(DiceGame & dicegame) const
	{
		dicegame.get_d1().roll();
		dicegame.get_d2().roll();
	}
};

#endif