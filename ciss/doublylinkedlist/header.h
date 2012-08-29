#ifndef DOUBLYLINKEDLISTNODE_H
#define DOUBLYLINKEDLISTNODE_H


class DoublyLinkedListNode
{
public:
	DoublyLinkedListNode(int _data = -9999, 
						 DoublyLinkedListNode * _next = 0,
						 DoublyLinkedListNode * _prev = 0)
		: data(_data), next(_next), prev(_prev)
	{}

	int & get_data() 
	{
		return data;
	}

	int get_data() const
	{
		return data;
	}

	void set_data(int _data)
	{
		data = _data;
	}

	DoublyLinkedListNode * get_prev() const
	{
		return prev;
	}

	void set_prev(DoublyLinkedListNode * _prev)
	{
		prev = _prev;
	}

	DoublyLinkedListNode * get_next() const
	{
		return next;
	}

	void set_next(DoublyLinkedListNode * _next)
	{
		next = _next;
	}

private:
	int data;
	DoublyLinkedListNode * prev;
	DoublyLinkedListNode * next;
};

std::ostream & operator<<(std::ostream & cout, const DoublyLinkedListNode & node)
{
	cout << '<' << &node << ": "
		 << node.get_data() << ", "
		 << node.get_prev() << ", "
		 << node.get_next() << '>'
		 << std::endl;

	return cout;
}


#endif