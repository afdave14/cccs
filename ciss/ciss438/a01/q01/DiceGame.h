#ifndef DICEGAME_H
#define DICEGAME_H


class Die 
{
public:
	void roll()
	{
		face_value = rand() % 6 + 1;
	}


	int get_face_value() const 
	{
		return face_value;
	}

private:
	int face_value;
};


class DiceGame 
{
public:
	void play() 
	{
		d1.roll();
		d2.roll();
	}


	int get_d1_face_value() const
	{
		return d1.get_face_value();
	}


	int get_d2_face_value() const
	{
		return d2.get_face_value();
	}

private:
	Die d1;
	Die d2;
};

#endif