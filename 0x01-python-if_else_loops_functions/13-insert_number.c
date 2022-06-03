#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head node
 * @number: integer
 * Return: address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *prev = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (*head == NULL)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (ptr->n > number)
	{
		*head = new;
		new->n = number;
		new->next = ptr;
		return (new);
	}
	while (ptr != NULL)
	{
		if (ptr->n >= number)
		{
			prev->next = new;
			new->n = number;
			new->next = ptr;
			return (new);
		}
		prev = ptr;
		ptr = ptr->next;
	}
	prev->next = new;
	new->n = number;
	new->next = NULL;
	return (new);
}
