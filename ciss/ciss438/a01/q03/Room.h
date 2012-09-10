#ifndef ROOM_H
#define ROOM_H

class Room {
public:
	Room() 
	{
		for (int i = 0; i < 4; i++)
			wall[i] = -1;
	}


	int get_room(int index) 
	{
		return wall[index];
	}


	void set_room(int dir, int room) 
	{
		wall[dir] = room;
	}


	Room operator=(Room r) 
	{
		for (int i = 0; i < 4; i++)
			wall[i] = r.wall[i];
	}

	
private:
	int wall[4];
};

#endif