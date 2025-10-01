from AVLTree import AVLTree

def main():
    tree = AVLTree()

    print("Тест AVL-дерева")

    # Вставка последовательности, вызывающей все 4 случая балансировки
    print("Вставляем: 10, 20, 30, 40, 50, 25")
    tree.insert(10)  # 10

    tree.insert(20)  #   10
                     #     \
                     #      20

    tree.insert(30)  # RR →    20
                     #        / \
                     #       10 30

    tree.insert(40) #       20
                    #      / \
                    #     10 30
                    #          \
                    #           40

    tree.insert(50)  # RR →  20
                     #       / \
                     #      10 40
                     #         / \
                     #        30 50

    tree.insert(25)  # RL →   30
                     #       / \
                     #      20 40
                     #     /   / \
                     #    10  25 50

    print("Обход: ", end="")
    tree.print_in_order()  # Ожидается: 10 20 25 30 40 50

    # Проверка поиска
    print("Проверка поиска")
    keys_to_test = [10, 25, 30, 35, 50, 100]
    for key in keys_to_test:
        if tree.contains(key):
            print(f"Ключ {key} найден.")
        else:
            print(f"Ключ {key} НЕ найден.")

    # Проверка find
    print("\nПроверка find")
    node = tree.find(25)
    if node:
        print(f"Найден узел с ключом: {node.key}")
        # Попробуем найти его детей
        left_child = node.left.key if node.left else "None"
        right_child = node.right.key if node.right else "None"
        print(f"Левый ребёнок: {left_child}")
        print(f"Правый ребёнок: {right_child}")

    # Попытка вставить дубликат
    print("\nВставка дубликата 25")
    tree.insert(25)
    print("Обход после вставки дубликата: ", end="")
    tree.print_in_order()  # Должен быть тот же: 10 20 25 30 40 50


if __name__ == "__main__":
    main()