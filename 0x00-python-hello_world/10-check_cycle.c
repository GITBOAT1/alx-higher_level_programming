#include "lists.h"

/**
 * check_cycle - This is just a simple func to tell there is a cycle
 * @list: this holds the values from the head node.
 * Return: return 0 if not a cycle
*/

int check_cycle(listint_t *list)
{
    listint_t *tmp = list;
    listint_t *cur = list->next;

    if (!list || !list->next)
    return (0);

    while (cur && cur->next)
    {
	cur = cur->next->next;
	tmp = tmp->next;
	if (tmp == cur)
	{
	     return (1);
	}
    }
    return (0);
}
