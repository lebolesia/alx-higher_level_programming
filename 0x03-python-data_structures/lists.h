#include <stddef.h>
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly link list
 * @n: integer
 * @next: shows the following node
 *
 * Description: singly link list node struct
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
