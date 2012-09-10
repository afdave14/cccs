#ifndef DUNGEON_H
#define DUNGEON_H
#include <vector>
#include "Room.h"


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


private:
	int num_rooms;
	std::vector< Room > room;
};

#endif