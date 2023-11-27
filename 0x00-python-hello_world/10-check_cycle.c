#include "lists.h"

/**
 * check_cycle - funct checks whether singly linked list has cycle in it
 * @list: pointer to start of node
 * Return: 0 if no cycle, 1 if cycle is present 
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
