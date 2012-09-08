#ifndef PLAYER_H
#define PLAYER_H

class Player {
public:
	void play(DiceGame dicegame){
		roll(dicegame.die1);
		roll(dicegame.die2);
	}
	void roll(Die die) {
		int x = rand() % 7 + 1;
		die.value = x;
	}
};

#endif