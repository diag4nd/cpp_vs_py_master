from BinaryTree import *
from tree_functions import *

mpl.use('Qt5Agg')


def main():
    bst = BinaryTree()
    for key in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(key)

    print(f"Is BST: {is_bst(bst)}")  # True
    visualize_binary_tree(bst, f"Is BST: {is_bst(bst)}")

    non_bst = BinaryTree()

    non_bst.root = Node(10)
    non_bst.root.left = Node(7)
    non_bst.root.right = Node(15)

    non_bst.root.left.left = Node(8)
    non_bst.root.left.right = Node(6)

    non_bst.root.right.left = Node(12)
    non_bst.root.right.right = Node(18)

    non_bst.root.left.right.left = Node(1)
    non_bst.root.right.left.left = Node(2)
    non_bst.root.right.left.right = Node(3)
    non_bst.root.right.right.right = Node(4)

    print(f"Is BST: {is_bst(non_bst)}")
    visualize_binary_tree(non_bst, f"Is BST: {is_bst(non_bst)}")


if __name__ == "__main__":
    main()
    plt.show()