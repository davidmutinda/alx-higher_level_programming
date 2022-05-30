#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *temp = list;

	if (list == NULL)
		return (0);
	while (current->next != NULL)
	{
		while (temp->next != NULL)
		{
			if (temp == list && list != head)
				break;

			else if (list->next == temp)
				return (1);

			temp = temp->next;
		}
		temp = head;
		list = list->next;
	}
	return (0);
}
