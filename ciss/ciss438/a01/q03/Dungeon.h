#ifndef DUNGEON_H
#define DUNGEON_H
#include <vector>
#include "Room.h"
#include "Person.h"


class Dungeon {
public:
	void create_room()
	{
		room.push_back(Room());
	}


	void join(int index_a, int index_b, int dir_a, int dir_b)
	{
		if (room[index_a].get_room(dir_a) != -1 || room[index_b].get_room(dir_b) != -1)
			std::cout << "ERROR: One or more rooms is already occupied!" << std::endl;
		else
		{
			room[index_a].set_room(dir_a, index_b);
			room[index_b].set_room(dir_b, index_a);
		}
	}


	void place_person(Person & person, int index)
	{
		if (index > room.size())
			std::cout << "WARNING: Room does not exist!" << std::endl;
		else
			person.set_pos(index);
	}


	void move_person(Person & person, int index)
	{
		int cp = person.get_pos();

		if (index > room.size())
		{
			std::cout << "WARNING: You have tried to access a room that does not exist!" << std::endl;
			return;
		}
		if (room[cp].get_room(0) != index && room[cp].get_room(1) != index 
			&& room[cp].get_room(2) != index && room[cp].get_room(3) != index)
			std::cout << "WARNING: The there is no path between the current room\nand the room you are trying to access!" << std::endl;
		else
			person.set_pos(index);
	}


private:
	std::vector< Room > room;
};

#endif