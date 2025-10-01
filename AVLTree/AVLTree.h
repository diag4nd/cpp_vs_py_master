#ifndef AVLTREE_H
#define AVLTREE_H

#include "Node.h"

class AVLTree
{
private:
    Node*   root;
    
    void    destruct            (Node*);
    void    do_print_in_order   (Node*);
    Node*   do_insert           (Node*, int);
    Node*   do_find             (Node*, int);
public:
    AVLTree     ();
    ~AVLTree    ();

    void    insert          (int);
    void    print_in_order  ();
    bool    contains        (int);
    Node*   find            (int);
};

#endif // AVLTREE_H

