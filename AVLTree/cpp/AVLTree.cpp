#include "AVLTree.h"
#include <iostream>

AVLTree::AVLTree ():
    root    (nullptr)
{}

void AVLTree::destruct (Node* _node)
{
    if (_node == nullptr)
        return;

    destruct(_node->left);
    destruct(_node->right);

    delete _node;
}

AVLTree::~AVLTree ()
{
    destruct(root);
}

Node* AVLTree::do_insert (Node* _node, int _key)
{
    if (_node == nullptr)
        return new Node(_key);

    if (_key < _node->key)
        _node->left = avl_insert(_node->left, _key);

    else if (_key > _node->key)
        _node->right = avl_insert(_node->right, _key);

    update_height(_node);

    int balance_factor = get_balance_factor(_node);

    if (balance_factor < -1)
    {
        // Случай LL
        if (_key < _node->left->key)
        {
            _node = rotate_right(_node);
        }
        // Случай LR
        else if (_key > _node->left->key)
        {
            _node->left = rotate_left(_node->left);           
            _node = rotate_right(_node);
        }
    }
    else if (balance_factor > 1)
    {
        // Случай RR
        if (_key > _node->right->key)
        {
            _node = rotate_left(_node);
        }
        // Случай RL
        else if (_key < _node->right->key)
        {
            _node->right = rotate_right(_node->right);
            _node = rotate_left(_node);
        }
    }

    return _node;
}

void AVLTree::insert (int _key)
{
    root = do_insert(root, _key);
}

void AVLTree::do_print_in_order (Node* _node)
{
    if (_node == nullptr)
        return;

    do_print_in_order(_node->left);

    std::cout << _node->key << " ";

    do_print_in_order(_node->right);
}

void AVLTree::print_in_order ()
{
    do_print_in_order(root);
    std::cout << "\n" << std::endl;
}

bool AVLTree::contains (int _key)
{
    return find(_key) != nullptr;
}

Node* AVLTree::do_find (Node* _node, int _key)
{
    if (_node == nullptr)
        return nullptr;

    if (_key == _node->key)
        return _node;
    
    else if (_key < _node->key)
        return do_find(_node->left, _key);
    
    else
        return do_find(_node->right, _key);
}

Node* AVLTree::find (int _key)
{
    return do_find(root, _key);
}
