from BinaryTree import *
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import deque

mpl.use('Qt5Agg')


def visualize_binary_tree(tree):
    if tree.root is None:
        print("Дерево пустое!")
        return

    # Создаем граф
    G = nx.Graph()

    # Обходим дерево в ширину для добавления узлов и ребер
    queue = deque([tree.root])
    positions = {}
    level_height = {}

    # Сначала собираем все узлы и определяем позиции
    current_level = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()

            # Добавляем узел в граф
            G.add_node(node.key)

            # Вычисляем позицию для отображения
            x_pos = i - level_size / 2  # Центрируем узлы на уровне
            y_pos = -current_level  # Отрицательное значение для верхнего расположения корня
            positions[node.key] = (x_pos, y_pos)
            level_height[node.key] = current_level

            # Добавляем детей в очередь
            if node.left:
                G.add_edge(node.key, node.left.key)
                queue.append(node.left)
            if node.right:
                G.add_edge(node.key, node.right.key)
                queue.append(node.right)

        current_level += 1

    # Создаем рисунок
    plt.figure(figsize=(6, 4), dpi=200)

    # Рисуем граф
    node_colors = ['lightgreen' for _ in G.nodes()]
    node_sizes = [800 for _ in G.nodes()]

    nx.draw(G, positions,
            with_labels=True,
            node_color=node_colors,
            node_size=node_sizes,
            font_size=10,
            font_weight='bold',
            arrows=False)

    plt.title("Binary Search Tree Visualization")
    plt.axis('off')


def is_bst(tree):
    """Проверяет, является ли дерево корректным BST"""

    def is_bst_helper(node, min_val, max_val):
        if node is None:
            return True

        # Проверяем, что значение узла находится в допустимом диапазоне
        if min_val is not None and node.key <= min_val:
            return False
        if max_val is not None and node.key >= max_val:
            return False

        # Рекурсивно проверяем левое и правое поддеревья
        return (is_bst_helper(node.left, min_val, node.key) and
                is_bst_helper(node.right, node.key, max_val))

    return is_bst_helper(tree.root, None, None)


def main():
    # Создаем корректное BST
    bst = BinaryTree()
    for key in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(key)

    print("In-order traversal:")
    bst.print_in_order()  # 2 3 4 5 6 7 8

    print(f"Is BST: {is_bst(bst)}")  # True

    # Проверяем поиск
    print(f"Contains 4: {bst.contains(4)}")  # True
    print(f"Contains 9: {bst.contains(9)}")  # False

    # Визуализация
    print("\n--- Визуализация BST ---")
    visualize_binary_tree(bst)

    # Дополнительный тест с другим деревом
    print("\n--- Тест с другим деревом ---")
    bst2 = BinaryTree()
    for key in [10, 5, 15, 3, 7, 12, 18]:
        bst2.insert(key)

    bst2.print_in_order()
    print(f"Is BST: {is_bst(bst2)}")
    visualize_binary_tree(bst2)


if __name__ == "__main__":
    main()
    plt.show()