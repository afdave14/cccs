#ifndef LINKEDLIST_H
#define LINKEDLIST_H


#include <iostream>
#include "header.h"


class ValueError
{};


class LinkedList
{
public:
	LinkedList()
		: head(NULL)
	{
		std::cout << "LinkedList constructor" << std::endl;
	}

	LinkedList(const LinkedList & list)
		: head(NULL)
	{
		*this = list;
	}

	~LinkedList()
	{
		clear();
	}

	void clear()
	{
		while (!is_empty())
		{
			remove_head();
		}
	}

	bool is_empty() const
	{
		return (head == NULL);
	}

	int remove_head()
	{
		if (head == NULL)
		{
			throw ValueError();
		}

		int ret = head->get_data();
		LinkedListNode * newHead = head->get_next();
		delete head;
		head = newHead;
		return ret;
	}

	void insert_head(int x)
	{
		LinkedListNode * node = new LinkedListNode(x, head);
		head = node;
	}

	void insert_tail(int x)
	{
		LinkedListNode * node = new LinkedListNode(x);

		if (is_empty())
		{
			head = node;
		}
		else
		{
			LinkedListNode * tail;
			tail = head;
			while (tail->get_next() != NULL)
			{
				tail = tail->get_next();
			}
			tail->set_next(node);
		}
	}

	bool operator==(const LinkedList & list) const
	{
		LinkedListNode * p = head;
		LinkedListNode * q = get_head();

		while (1)
		{
			if (p == NULL && q == NULL)
			{
				return true;
			}

			if ((p == NULL && q != NULL) || (p != NULL && q == NULL))
			{
				return false;
			}

			if (p->get_data() != q->get_data())
			{
				return false;
			}

			p = p->get_next();
			q = q->get_next();
		}
	}

	bool operator!=(const LinkedList & list) const
	{
		return !(*this == list);
	}

	LinkedList & operator=(const LinkedList & list)
	{
		if (this == &list)
		{
			return *this;
		}

		clear();
		LinkedListNode * p = list.get_head();
		while (p != NULL)
		{
			insert_tail(p->get_data());
			p = p->get_next();
		}
		return (*this);
	}

	LinkedListNode * get_head() const
	{
		return head;
	}

	LinkedListNode * find(int x)
	{
		LinkedListNode * p = head;
		while (p != NULL)
		{
			if (p->get_data() == x)
			{
				return p;
			}
			p = p->get_next();
		}
		return p;
	}

	LinkedListNode * prev(const LinkedListNode * p) const
	{
		if (head == NULL)
		{
			return false;
		}
		else if (p == head)
		{
			return NULL;
		}
		else
		{
			LinkedListNode * previous = head;
			LinkedListNode * next = previous->get_next();

			while (next != p)
			{
				if (next == NULL)
				{
					return false;
				}

				previous = next;
				next = previous->get_next();
			}
			return previous;
		}
	}

	int remove(LinkedListNode * p)
	{
		LinkedListNode * previous = prev(p);

		if (previous == NULL)
		{
			if (p == head)
			{
				return remove_head();
			}
			else
			{
				throw ValueError();
			}
		}
		else
		{
			int ret = p->get_data();
			previous->set_next(p->get_next());
			delete p;
			return ret;
		}
	}

	int remove(int x)
	{
		return remove(find(x));
	}

	int size() const
	{
		int count = 0;
		LinkedListNode * p = head;

		while (p != NULL)
		{
			count++;
			p = p->get_next();
		}
		return count;
	}

	int operator[](int i) const
	{
		if (i < 0)
		{
			throw ValueError();
		}

		LinkedListNode * p = head;
		for (int j = 0; j < i; j++)
		{
			if (p == NULL)
			{
				throw ValueError();
			}
			p = p->get_next();
		}

		if (p == NULL)
		{
			throw ValueError();
		}
		else
		{
			return p->get_data();
		}
	}

private:
	LinkedListNode * head;
};

std::ostream & operator<<(std::ostream & cout, const LinkedList & x)
{
	int size = x.size();
	cout << '[';
	if (size > 0)
	{
		for (int i = 0; i < size - 1; i++)
		{
			cout << x[i] << ", ";
		}
		cout << x[size - 1];
	}
	cout << ']' << std::endl;

	return cout;
}


#endif