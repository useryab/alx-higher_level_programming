#ifndef LISTS_H
#define LISTS_H

<<<<<<< HEAD
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
=======
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 *  * struct listint_s - singly linked list
 *   * @n: integer
 *    * @next: points to the next node
 *     *
 *      * Description: singly linked list node structure
 *       * for notrebloh project
 *        */
typedef struct listint_s
{
		int n;
			struct listint_s *next;
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
