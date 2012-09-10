#ifndef PERSON_H
#define PERSON_H

class Person {
public:
	int get_pos() const
	{
		return pos;
	}


	void set_pos(int index)
	{
		pos = index;
	}


private:
	int pos;
};

#endif