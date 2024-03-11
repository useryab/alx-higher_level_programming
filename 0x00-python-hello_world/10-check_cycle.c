#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle: checks if a list contains a cycle
 * @list: singly-linked list
 * Return: if there is a cycle  1
 *         if not then 0
*/
int check_cycle(listint_t *list);
{
    listint_s *turtle, *hare;

    if(list == NULL || list->next == NULL)
            return (0);
    turtle = list->next;
    hare = list->next;

    while (turtle && hare && hare->next)
    {
        if (turtle == hare)
                return (1);
        turtle = turtle->next;
        hare = hare->next->next
    }

        return (0)
}
