#include "lists.h"
/**
 * check_cycle - checks if a cycle is present in list
 * @list: list object
 * Return: 1 if cycle present, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *d;

	if (!list)
	{
		return (0);
	}
	s = list;
	d = list->next;
	while (d && s && d->next)
	{
		if (s == d)
		{
			return (1);
		}
		s = s->next;
		d = d->next->next;
	}
	return (0);
}
