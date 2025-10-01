from Node import Node

class AVLTree:
    def __init__(self):
        self.root = None

    # def destruct(self, node):
    #     if node is None:
    #         return
    #
    #     self.destruct(node.left)
    #     self.destruct(node.right)
    #
    #     del node

    # def __del__(self):
    #     self.destruct(self.root)

    def update_height(self, node):
        if node is None:
            return 0

        left_height = self.update_height(node.left) if node.left else 0
        right_height = self.update_height(node.right) if node.right else 0

        node.height = max(left_height, right_height) + 1
        return node.height

    @staticmethod
    def get_balance_factor(node):
        if node is None:
            return 0

        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        return right_height - left_height

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    def do_insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.do_insert(node.left, key)
        elif key > node.key:
            node.right = self.do_insert(node.right, key)

        self.update_height(node)

        balance_factor = self.get_balance_factor(node)

        if balance_factor < -1:
            # Случай LL
            if key < node.left.key:
                node = self.rotate_right(node)
            # Случай LR
            elif key > node.left.key:
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
        elif balance_factor > 1:
            # Случай RR
            if key > node.right.key:
                node = self.rotate_left(node)
            # Случай RL
            elif key < node.right.key:
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)

        return node

    def insert(self, key):
        self.root = self.do_insert(self.root, key)

    def do_print_in_order(self, node):
        if node is None:
            return

        self.do_print_in_order(node.left)

        print(node.key, end=" ")

        self.do_print_in_order(node.right)

    def print_in_order(self):
        self.do_print_in_order(self.root)
        print("\n")

    def contains(self, key):
        return self.find(key) is not None

    def do_find(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node

        elif key < node.key:
            return self.do_find(node.left, key)

        else:
            return self.do_find(node.right, key)

    def find(self, key):
        return self.do_find(self.root, key)