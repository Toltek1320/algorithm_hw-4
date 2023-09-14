# Доработать бинарное дерево с семинара, добавить подсчет количества элементов, вывод всего дерева на экран, удаление элемента.
# Должна быть документация к классам и методам.

class Node:
    def __init__(self, value): # конструктор класса, создает узел с заданным значением. Инициализирует атрибуты left и right как None.
        self.value = value
        self.left = None
        self.right = None

    def __str__(self): # возвращает строковое представление значения узла и значений его дочерних узлов (если они существуют).
        res = f'Значение узла: {self.value}'
        if self.left:
            res += f', значение левого: {self.left.value}'
        if self.right:
            res += f', значение правого: {self.right.value}'
        return res

class BinaryTree:
    def __init__(self, root_value): # конструктор класса, создает бинарное дерево с корневым узлом, содержащим заданное значение. 
        # Инициализирует атрибут count как 1.
        self.root = Node(root_value)
        self.count = 1

    def add(self, value): # добавляет новый узел со значением value в бинарное дерево. 
        # Если значение уже существует, выводит сообщение "Такое значение уже существует".
        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    self.count += 1
                    break
            elif value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    self.count += 1
                    break
            else:
                print("Такое значение уже существует")
                break

    def search(self, value): # ищет и возвращает узел с заданным значением value в бинарном дереве. 
        # Если значение не найдено, возвращает None.
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
        return None

    def delete(self, value): # удаляет узел с заданным значением value из бинарного дерева. 
            # Если значение не найдено, выводит сообщение "Такого значения нет в дереве".
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def delete_node(node, value): 
            if node is None:
                return None
            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    min_right = find_min(node.right)
                    node.value = min_right.value
                    node.right = delete_node(node.right, min_right.value)
            return node

        if self.search(value):
            self.root = delete_node(self.root, value)
            self.count -= 1
        else:
            print("Такого значения нет в дереве")

    def print_tree(self): # выводит все узлы бинарного дерева в отсортированном порядке.
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            print(node)
            inorder(node.right)

        inorder(self.root)

    def get_count(self): # возвращает количество элементов в бинарном дереве.
        return self.count

bt = BinaryTree(5) # создает новое бинарное дерево с корневым узлом, содержащим значение 5.
bt.add(10) # добавляет новый узел со значением 10 в бинарное дерево.
bt.add(15) # добавляет новый узел со значением 15 в бинарное дерево.
bt.add(3) # добавляет новый узел со значением 3 в бинарное дерево.
bt.add(4) # добавляет новый узел со значением 4 в бинарное дерево.

print(bt.root) # выводит корневой узел бинарного дерева.
print(bt.root.left) # выводит левый дочерний узел корневого узла бинарного дерева.
print(bt.root.right) # выводит правый дочерний узел корневого узла бинарного дерева.
print(bt.get_count()) # выводит количество элементов в бинарном дереве.

bt.delete(10) # удаляет узел со значением 10 из бинарного дерева.
bt.print_tree() # выводит все узлы бинарного дерева.
print(bt.get_count()) # выводит количество элементов в бинарном дереве.