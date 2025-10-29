from Node import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def do_insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.do_insert(node.left, key)
        elif key > node.key:
            node.right = self.do_insert(node.right, key)

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
        print()

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