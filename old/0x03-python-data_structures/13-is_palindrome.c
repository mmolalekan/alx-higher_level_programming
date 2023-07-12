#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: entry point
* Return: 1 if it is a palindrome, 0 if it is not a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	/* Find the middle of the list using the two-pointer technique */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	/**
	*If the list has odd number of nodes,
	* move the slow pointer one step forward
	*/
	if (fast != NULL)
		slow = slow->next;

    /* Compare the first half of the list (prev) with the second half (slow) */
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}

