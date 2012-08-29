#ifndef LINKEDLISTNODE_H
#define LINKEDLISTNODE_H


class LinkedListNode
{
public:
	LinkedListNode(int _data = -9999, LinkedListNode * _next = 0)
		: data(_data), next(_next)
	{}

	int get_data() const
	{
		return data;
	}

	void set_data(int _data)
	{
		data = _data;
	}

	LinkedListNode * get_next() const
	{
		return next;
	}

	void set_next(LinkedListNode * _next)
	{
		next = _next;
	}

private:
	int data;
	LinkedListNode * next;
};

std::ostream & operator<<(std::ostream & cout, const LinkedListNode & node)
{
	cout << '<' << &node << ": "
		 << node.get_data() << ", "
		 << node.get_next() << '>'
		 << std::endl;

	return cout;
}


#endif