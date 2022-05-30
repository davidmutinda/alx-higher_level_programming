#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	while (1)
	{
		if (list == NULL)
			return (0);
		if (list->next == head)
			return (1);
		list = list->next;
	}
}
