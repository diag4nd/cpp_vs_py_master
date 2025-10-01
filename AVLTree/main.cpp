#include "AVLTree.h"
#include <iostream>

int main() {
    AVLTree tree;

    std::cout << "=== Тест AVL-дерева ===\n";

    // Вставка последовательности, вызывающей все 4 случая балансировки
    std::cout << "Вставляем: 10, 20, 30, 40, 50, 25\n";
    tree.insert(10); //       10

    tree.insert(20); //       10
                     //        \
                     //         20
    
    tree.insert(30); // RR →   20
                     //        / \
                     //       10 30
    
    tree.insert(40); //       20
                     //      / \
                     //     10 30
                     //          \
                     //           40
    
    tree.insert(50); // RR →  20
                     //      / \
                     //     10 40
                     //        / \
                     //       30 50
    
    tree.insert(25); // RL →  30
                     //       / \
                     //      20 40
                     //     /   / \
                     //    10  25 50

    std::cout << "Обход: ";
    tree.print_in_order(); // Ожидается: 10 20 25 30 40 50

    // Проверка поиска
    std::cout << "\nПроверка поиска\n";
    int keys_to_test[] = {10, 25, 30, 35, 50, 100};
    for (int key : keys_to_test) {
        if (tree.contains(key)) {
            std::cout << "Ключ " << key << " найден.\n";
        } else {
            std::cout << "Ключ " << key << " НЕ найден.\n";
        }
    }

    // Проверка find
    std::cout << "\nПроверка find\n";
    Node* node = tree.find(25);
    if (node) {
        std::cout << "Найден узел с ключом: " << node->key << "\n";
        // Попробуем найти его детей
        std::cout << "Левый ребёнок: " << (node->left ? std::to_string(node->left->key) : "nullptr") << "\n";
        std::cout << "Правый ребёнок: " << (node->right ? std::to_string(node->right->key) : "nullptr") << "\n";
    }

    // Попытка вставить дубликат
    std::cout << "\nВставка дубликата 25\n";
    tree.insert(25);
    std::cout << "Обход после вставки дубликата: ";
    tree.print_in_order(); // Должен быть тот же: 10 20 25 30 40 50

    return 0;
}
