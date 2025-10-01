
class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


def get_height(node: Node) -> int:
    if node is None:
        return 0
    else:
        return node.height


def update_height(node: Node):
    height = 1 + max(get_height(node.left), get_height(node.right))
    node.height = height


def get_balance_factor(node: Node) -> int:
    balance_factor = get_height(node.right) - get_height(node.left)
    return balance_factor


def rotate_right(node_y: Node) -> Node:
    #      y
    #     / \
    #    x   c
    #   / \
    #  a   b
    #
    # После поворота:
    #      x
    #     / \
    #    a   y
    #       / \
    #      b   c
    node_x = node_y.left
    node_b = node_x.right

    node_x.right = node_y
    node_y.left = node_b

    update_height(node_y)
    update_height(node_x)

    return node_x


def rotate_left(node_x: Node) -> Node:
    #      x
    #     / \
    #    a   y
    #       / \
    #      b   c
    #
    # После поворота:
    #      y
    #     / \
    #    x   c
    #   / \
    #  a   b
    node_y = node_x.right
    node_b = node_y.left

    node_y.left = node_x
    node_x.right = node_b

    update_height(node_x)
    update_height(node_y)

    return node_y


def bst_insert(node: Node, key: int) -> Node:
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = bst_insert(node.left, key)
    elif key > node.key:
        node.right = bst_insert(node.right, key)

    return node


def avl_insert(node: Node, key: int) -> Node:
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = avl_insert(node.left, key)
    elif key > node.key:
        node.right = avl_insert(node.right, key)

    update_height(node)
    balance_factor = get_balance_factor(node)

    if balance_factor < -1:
        # LL
        if key < node.left.key:
            node = rotate_right(node)
        # LR
        elif key > node.left.key:
            node.left = rotate_left(node.left)
            node = rotate_right(node)

    elif balance_factor > 1:
        # RR
        if key > node.right.key:
            node = rotate_left(node)
        # RL
        elif key < node.right.key:
            node.right = rotate_right(node.right)
            node = rotate_left(node)

    return node
