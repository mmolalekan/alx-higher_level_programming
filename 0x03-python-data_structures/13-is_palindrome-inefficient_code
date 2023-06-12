#include "lists.h"

/**
* listint_len - returns the number of elements in a linked listint_t list.
* @h: the head of the linked list
* Return: the number of elements
*/

size_t listint_len(const listint_t *h)
{
	const listint_t *temp;
	size_t count;

	temp = h;
	count  = 0;
	while (temp != NULL)
	{
		temp = temp->next;
		count++;
	}
	return (count);
}

/**
* get_dataint_at_index - returns the data of a listint_t linked list.
* @head: entry into the linked list
* @index: the index of the node, starting at 0
* Return: the nth data on success, NULL on failure
*/

unsigned int get_dataint_at_index(listint_t *head, unsigned int index)
{
	listint_t *temp;
	unsigned int i;

	if (head == NULL)
	{
		exit(98);
	}

	temp = head;
	for (i = 0; i < index; i++)
	{
		if (temp->next == NULL)
		{
			exit(98);
		}
		temp = temp->next;
	}
	return (temp->n);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: entry point
* Return: 1 if it is a palindrome, 0 if it is not a palindrome
*/

int is_palindrome(listint_t **head)
{
	unsigned int count, part_1, part_2, i = 0, j;

	count = j = listint_len(*head);
	while (i < (count / 2))
	{
		part_1 = get_dataint_at_index(*head, i);
		part_2 = get_dataint_at_index(*head, j - 1);
		if (part_1 != part_2)
			return (0);
		i++;
		j--;
	}
	return (1);
}
