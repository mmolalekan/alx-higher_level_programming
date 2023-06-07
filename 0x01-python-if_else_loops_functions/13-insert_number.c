#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: Pointer to the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (!*head || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	node = *head;
	while (node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
