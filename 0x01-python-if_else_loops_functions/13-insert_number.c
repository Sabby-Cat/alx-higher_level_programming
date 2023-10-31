#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a new node at position
 * @head: array
 * @number: position
 * Return: array or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	if (*head == NULL)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	else if (number <= (*head)->n)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		tmp = *head;
		while (tmp->next != NULL && number > tmp->next->n)
		{
			tmp = tmp->next;
		}
		new->n = number;
		new->next = tmp->next;
		tmp->next = new;
		return (new);
	}
	return (NULL);

}
