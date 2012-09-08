#ifndef DUNGEON_H
#define DUNGEON_H

#include "Room.h"

class Dungeon {
public:
	Dungeon(int _num_rooms) : num_rooms(_num_rooms) {
		room = new Room[_num_rooms];
	}
	Dungeon(const Dungeon & d) {
		if (num_rooms != d.num_rooms)
			std::cout << "CANNOT COPY" << std::endl;
		for (int i = 0; i < num_rooms; i++)
			room[i] = d.room[i];
	}

	void join(int index_a, int index_b, int dir_a, int dir_b) {
		if (room[index_a].get_room(dir_a) != -1 || room[index_b].get_room(dir_b) != -1)
			std::cout << "ERROR: One or more rooms is already occupied!" << std::endl;
		room[index_a].set_room(dir_a, index_b);
		room[index_b].set_room(dir_b, index_a);
	}
	~Dungeon() {
		delete [] room;
	}
private:
	int num_rooms;

	Room *room;
};

#endif