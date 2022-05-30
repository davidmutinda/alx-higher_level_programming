#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *reg = list;

	if (list == NULL)
		return (0);
	while (current->next != NULL)
	{
		reg = reg->next;
		current = current->next->next;
		if (current == reg)
			return (1);
	}
	return (0);
}
