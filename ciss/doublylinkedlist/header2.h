#ifndef DOUBLYLINKEDLIST_H
#define DOUBLYLINKEDLIST_H


#include <iostream>
#include "header.h"


class ValueError
{};


class DoublyLinkedList
{
public:
	DoublyLinkedList()
		: head(new DoublyLinkedListNode(-9999)),
		  tail(new DoublyLinkedListNode(9999))
	{
		head->set_next(tail);
		tail->set_prev(head);
	}

	DoublyLinkedList(const DoublyLinkedList & list)
		: head(new DoublyLinkedListNode(-9999)),
		  tail(new DoublyLinkedListNode(9999))
	{
		head->set_next(tail);
		tail->set_prev(head);
		*this = list;
	}

	~DoublyLinkedList()
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
		return (head->get_next() == tail);
	}

	int remove_head()
	{
		if (is_empty())
		{
			throw ValueError();
		}

		return remove(get_head());
	}

	int remove_tail()
	{
		if (is_empty())
		{
			throw ValueError();
		}

		return remove(get_tail());
	}

	int remove(DoublyLinkedListNode * p)
	{
		if (p == NULL)
		{
			throw ValueError();
		}

		DoublyLinkedListNode * p_prev = p->get_prev();
		DoublyLinkedListNode * p_next = p->get_next();

		int ret = p->get_data();
		p_prev->set_next(p_next);
		p_next->set_prev(p_prev);
		delete p;
		return ret;
	}

	void insert_after(DoublyLinkedListNode * p, int x)
	{
		DoublyLinkedListNode * r = p->get_next();
		DoublyLinkedListNode * q = new DoublyLinkedListNode(x, r, p);

		r->set_prev(q);
		p->set_next(q);
	}

	void insert_before(DoublyLinkedListNode * p, int x)
	{
		DoublyLinkedListNode * r = p->get_prev();
		DoublyLinkedListNode * q = new DoublyLinkedListNode(x, p, r);

		r->set_next(q);
		p->set_prev(q);
	}

	void insert_head(int x)
	{
		insert_after(head, x);
	}

	void insert_tail(int x)
	{
		insert_before(tail, x);
	}

	bool operator==(const DoublyLinkedList & list) const
	{
		DoublyLinkedListNode * tail_sentinel = get_tail_sentinel();
		DoublyLinkedListNode * list_tail_sentinel = list.get_tail_sentinel();

		DoublyLinkedListNode * p = get_head();
		DoublyLinkedListNode * q = list.get_head();

		while (1)
		{
			if (p == tail_sentinel && q == list_tail_sentinel)
			{
				return true;
			}

			if ((p == tail_sentinel && q != list_tail_sentinel) ||
				(p != tail_sentinel && q == list_tail_sentinel))
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

	bool operator!=(const DoublyLinkedList & list) const
	{
		return !(*this == list);
	}

	DoublyLinkedList & operator=(const DoublyLinkedList & list)
	{
		if (this == &list)
		{
			return (*this);
		}

		clear();
		DoublyLinkedListNode * p = list.get_head();
		while (p != list.get_tail_sentinel())
		{
			insert_tail(p->get_data());
			p = p->get_next();
		}
		return (*this);
	}

	DoublyLinkedListNode * find(int x)
	{
		DoublyLinkedListNode * p = head->get_next();

		while (p != tail)
		{
			if (p->get_data() == x)
			{
				return p;
			}
			p = p->get_next();
		}

		return (p == tail ? NULL : p);
	}

	int remove(int x)
	{
		return remove(find(x));
	}

	int size() const
	{
		int count = 0;
		DoublyLinkedListNode * p = head->get_next();

		while (p != tail)
		{
			count++;
			p = p->get_next();
		}
		return count;
	}

	int & operator[](int i) const
	{
		if (i < 0)
		{
			throw ValueError();
		}

		DoublyLinkedListNode * p = head->get_next();
		for (int j = 0; j < i; j++)
		{
			if (p == tail)
			{
				throw ValueError();
			}
			p = p->get_next();
		}

		if (p == tail)
		{
			throw ValueError();
		}
		else
		{
			return p->get_data();
		}
	}

	DoublyLinkedListNode * get_head() const
	{
		return head->get_next();
	}

	DoublyLinkedListNode * get_tail() const
	{
		return tail->get_prev();
	}

	DoublyLinkedListNode * get_head_sentinel() const
	{
		return head;
	}

	DoublyLinkedListNode * get_tail_sentinel() const
	{
		return tail;
	}

private:
	DoublyLinkedListNode * head;
	DoublyLinkedListNode * tail;
};

std::ostream & operator<<(std::ostream & cout, const DoublyLinkedList & list)
{
	cout << '[';
	DoublyLinkedListNode * p = list.get_head();
	while (p != list.get_tail_sentinel())
	{
		cout << p->get_data();
		if (p != list.get_tail())
		{
			cout << ", ";
		}
		p = p->get_next();
	}
	cout << ']' << std::endl;

	return cout;
}


#endif