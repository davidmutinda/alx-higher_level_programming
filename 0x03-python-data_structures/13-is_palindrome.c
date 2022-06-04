#include "lists.h"
/**
 * is_palindrome - checks if linked list is palindrome
 * @head: pointer to head of linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	listint_t *rev;
	listint_t *hld;

	if (*head == NULL)
	{
		return (0);
	}
	rev = malloc(sizeof(listint_t));
	hld = rev;
	rev->n = ptr->n;
	rev = malloc(sizeof(listint_t));
	hld->next = NULL;
	ptr = ptr->next;
	while (ptr != NULL)
	{
		rev->n = ptr->n;
		rev->next = hld;
		hld = rev;
		rev = malloc(sizeof(listint_t));
		ptr = ptr->next;
	}
	free(rev);
	ptr = *head;
	rev = hld;

	while (ptr != NULL)
	{
		if (rev->n != ptr->n)
			return (0);
		ptr = ptr->next;
		hld = rev;
		rev = rev->next;
	}
	return (1);
}
