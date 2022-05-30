#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;

	if (head == NULL)
		return (0);
	while(1)
	{
		if (list->next == head)
			return (1);
		if (list->next == NULL)
			return(0);
		list = list->next;
	}
}
