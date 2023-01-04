#include "lists.h"

/**
  * insert_node - a function that inserts a node on a sorted linked list
  * @head: pointer to first pointer
  * @number: value to be stored in the node
  * Return: pointer to new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;

	return (new);
}
