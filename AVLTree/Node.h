// Node.h
#ifndef NODE_H
#define NODE_H

struct Node
{
    int     key;
    int     height;
    Node*   left;
    Node*   right;

    Node (int _key_);
};

int     get_height          (Node*);
void    update_height       (Node*);
int     get_balance_factor  (Node*);

Node*   rotate_right        (Node*);
Node*   rotate_left         (Node*);
Node*   bst_insert          (Node*, int);
Node*   avl_insert          (Node*, int);

#endif // NODE_H
