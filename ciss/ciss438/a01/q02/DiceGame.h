#ifndef DICEGAME_H
#define DICEGAME_H

class Die {
public:
	int value;
};

class DiceGame {
public:
	void play(){
		int x = rand() % 7 + 1;
		int y = rand() % 7 + 1;
		die1.value = x, die2.value = y;
	}
	Die die1;
	Die die2;
};

#endif