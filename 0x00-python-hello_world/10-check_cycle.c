#include "lists.h"

/**
  * check_cycle - a function that checks whether a cycle exists
  * @list: linked list to check
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (!list)
		return (0);
	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
