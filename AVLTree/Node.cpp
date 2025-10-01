// Node.h
#include "Node.h"
#include <algorithm>

Node::Node (int _key): 
    key     (_key), 
    height  (1), 
    left    (nullptr), 
    right   (nullptr) 
{};

int get_height (Node* _node)
{
    if (_node == nullptr)
        return 0;
    else
        return _node->height;
}

void update_height (Node* _node)
{
    int height = 1 + std::max(get_height(_node->left), get_height(_node->right));
    
    _node->height = height; 
}

int get_balance_factor (Node* _node)
{
    int balance_factor = get_height(_node->right) - get_height(_node->left);

    return balance_factor;
}

Node* rotate_right (Node* _node_y)
{
    // Предполагается следующая входная структура:
    //
    //      y
    //     / \
    //    x   c
    //   / \
    //  a   b
    //
    // Правый поворот вокруг узла y приводит к следующей структуре:
    //
    //      x
    //     / \
    //    a   y
    //       / \
    //      b   c
    //

    Node* node_x = _node_y->left;
    Node* node_b = node_x->right;

    node_x->right   = _node_y;
    _node_y->left   = node_b;

    update_height(_node_y);
    update_height(node_x);

    return node_x;
}

Node* rotate_left (Node* _node_x)
{
    // Предполагается следующая входная структура:
    //
    //      x
    //     / \
    //    a   y
    //       / \
    //      b   c
    //
    // Левый поворот вокруг узла x приводит к следующей структуре:
    //
    //      y
    //     / \
    //    x   c
    //   / \
    //  a   b
    //

    Node* node_y = _node_x->right;
    Node* node_b = node_y->left;

    node_y->left    = _node_x;
    _node_x->right  = node_b;

    update_height(_node_x);
    update_height(node_y);

    return node_y;
}

Node* bst_insert (Node* _node, int _key)
{
    if (_node == nullptr)
        return new Node(_key);
    
    if (_key < _node->key)
        _node->left = bst_insert(_node->left, _key);
    
    else if (_key > _node->key)
        _node->right = bst_insert(_node->right, _key);

    return _node;
}

Node* avl_insert (Node* _node, int _key)
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


