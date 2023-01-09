#include "lists.h"

/**
  * is_palindrome - a function that checks if a singly linked list is a
  * palindrome.
  * @head: pointer to head pointer
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	int i, j, *array, k = 0;
	listint_t *first;

	first = *head;
	for (i = 0; first != NULL; i++)
		first = first->next;
	array = malloc(sizeof(int) * i);
	first = *head;
	while (first != NULL)
	{
		array[k++] = first->n;
		first = first->next;
	}

	for (j = 0; j <= (i / 2); j++)
	{
		if (array[j] != array[i - 1 - j])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
