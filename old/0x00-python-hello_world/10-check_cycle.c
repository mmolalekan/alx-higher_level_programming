#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *runner = list;

	if (!list)
	return (0);

	while (current && runner && runner->next)
	{
		current = current->next;
		runner = runner->next->next;
		if (current == runner)
		return (1);
	}

	return (0);
}

