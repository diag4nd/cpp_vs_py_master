from BinaryTree import *
from Node import *
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import deque

def is_bst_helper(node: Node, min_val: int, max_val: int):
    if node is None:
        return True

    if min_val is not None and node.key <= min_val:
        return False
    if max_val is not None and node.key >= max_val:
        return False

    return (is_bst_helper(node.left, min_val, node.key) and
            is_bst_helper(node.right, node.key, max_val))


def is_bst(tree: BinaryTree) -> bool:
    return is_bst_helper(tree.root, None, None)


def visualize_binary_tree(tree: BinaryTree, title):
    if tree.root is None:
        print("Дерево пустое!")
        return

    G = nx.Graph()

    queue = deque([tree.root])
    positions = {}
    level_height = {}

    left_edges = []
    right_edges = []

    current_level = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()

            # Добавляем узел в граф
            G.add_node(node.key)

            x_pos = i - level_size / 2  # Центрируем узлы на уровне
            y_pos = -current_level  # Отрицательное значение для верхнего расположения корня
            positions[node.key] = (x_pos, y_pos)
            level_height[node.key] = current_level

            if node.left:
                G.add_edge(node.key, node.left.key)
                left_edges.append((node.key, node.left.key))
                queue.append(node.left)
            if node.right:
                G.add_edge(node.key, node.right.key)
                right_edges.append((node.key, node.right.key))
                queue.append(node.right)

        current_level += 1

    plt.figure(figsize=(6, 4), dpi=200)

    node_colors = ['lightgreen' for _ in G.nodes()]
    node_sizes = [800 for _ in G.nodes()]

    nx.draw_networkx_nodes(G, positions,
                           node_color=node_colors,
                           node_size=node_sizes)

    nx.draw_networkx_labels(G, positions,
                            font_size=10,
                            font_weight='bold')

    nx.draw_networkx_edges(G, positions,
                           edgelist=left_edges,
                           edge_color='blue',
                           width=2,
                           style='solid',
                           label='Left child')

    nx.draw_networkx_edges(G, positions,
                           edgelist=right_edges,
                           edge_color='red',
                           width=2,
                           style='solid',
                           label='Right child')

    plt.title(title)
    plt.axis('off')

    plt.legend(loc='upper right')

