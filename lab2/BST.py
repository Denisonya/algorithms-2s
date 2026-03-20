"""
Бинарное дерево поиска (Binary Search Tree = BST)
Структура данных, представляющая собой бинарное дерево, в котором для каждой вершины выполняется следующее свойство:
Для любой вершины v дерева: v.left < v ≤ v.right, где
v.left - значения в левом поддереве / v.right - значения в правом поддереве
Замечание: если используется строгий знак v < v.right, то все значения в дереве уникальны.
Схема:
             (v)
            /   \
     (v.left)  (v.right)
Левое поддерево содержит элементы меньше v, правое поддерево содержит элементы больше либо равные v.
"""

"""
Атрибут узла parent нужен для итеративной реализации деревьев, чтобы мы знали путь обратно до входного узла, то есть с какого узла начинали.
При рекурсивной реализации деревьев, стек будет возвращать нас к предыдущему узлу.
"""


class Node:
    def __init__(self, key):
        self.key = key  # значение узла
        self.left = None  # ссылка на левого ребенка
        self.right = None  # ссылка на правого ребенка
        self.parent = None  # ссылка на родителя ребенка


class BinarySearchTree:
    def __init__(self):
        self.root = None  # ссылка на корень дерева

    def find_min(self, runner):
        """
        Поиск минимума в произвольном поддереве

        Сложность: O(h), где h — высота дерева
        """
        # идем до упора влево
        while runner.left:
            runner = runner.left

        return runner  # возвращаем найденный узел

    def find_max(self, runner):
        """
        Поиск максимума в произвольном поддереве

        Сложность: O(h), где h — высота дерева
        """
        # идем до упора вправо
        while runner.right:
            runner = runner.right

        return runner  # возвращаем найденный узел

    def search(self, runner, key):
        """
        Поиск элемента в произвольном поддереве

        Сложность: O(h), где h — высота дерева
        """
        while runner:  # пока не дошли до листа поддерева
            # если ключ меньше
            if key < runner.key:
                # идем влево
                runner = runner.left
            # если ключ больше
            elif key > runner.key:
                # идем вправо
                runner = runner.right
            # если нашли ключ
            else:
                return runner

        return None  # если не нашли узла с таким ключом

    def range_search(self, runner, lower_bound, right_bound, result):
        """
        RangeSearch(lower_bound, right_bound) в произвольном поддереве -> lower_bound <= искомые узлы <= right_bound

        Алгоритм:
        - если runner < lower_bound -> идти вправо
        - если runner > right_bound -> идти влево
        - если внутри диапазона -> добавить

        Сложность: O(log(n)), где n - кол-во узлов
        """
        # если поддерево пусто
        if runner is None:
            return

        # если ключ узла больше нижней границы
        if runner.key > lower_bound:
            self.range_search(runner.left, lower_bound, right_bound, result)
        # если ключ узла попадает в нижней границы
        if lower_bound <= runner.key <= right_bound:
            result.append(runner.key)
        # если ключ узла меньше нижней границы
        if runner.key < right_bound:
            self.range_search(runner.right, lower_bound, right_bound, result)

    def insert(self, key):
        """
        Вставка узла в дерево

        Замечание: узел всегда добавляется в листья

        Сложность: O(h), где h — высота дерева
        """
        new_node = Node(key)  # создаем новый узел

        # если дерево пустое
        if self.root is None:
            # новый узел становится корнем
            self.root = new_node
            return new_node

        runner = self.root  # устанавливаем бегунок, которым будем проходить по дереву
        parent = None  # переменная для отслеживания родителя

        # ищем место для вставки

        # идем по дереву
        while runner:
            # запоминаем родителя, то есть откуда пришли
            parent = runner

            if key < runner.key:
                runner = runner.left
            elif key > runner.key:
                runner = runner.right
            else:
                return runner  # вариант, когда нужно, чтобы все элементы дерева были уникальны
                # вариант, когда допускается повтор элементов дерева → продолжаем идти вправо

        # вставка

        new_node.parent = parent  # назначаем родителя для нового узла

        if key < parent.key:
            # вставка слева
            parent.left = new_node
        else:
            # вставка справа
            parent.right = new_node

        return new_node

    def replace_subtree(self, prev, new):
        """
        Замена поддерева prev на поддерево new, сохраняя все связи с родителями

        Сложность: O(1)
        """
        # если prev - корень дерева, то после замены новый корень становится new
        if prev.parent is None:
            self.root = new
        # если prev левый ребенок родителя
        elif prev == prev.parent.left:
            prev.parent.left = new  # родитель prev теперь указывает на new вместо prev
        # если prev правый ребенок родителя
        else:
            prev.parent.right = new  # родитель prev теперь указывает на new вместо prev

        # если new не None, устанавливаем его parent в родителя prev
        if new:
            new.parent = prev.parent

        # Замечание: объект, на который ссылается prev, будет удален GC'ом после заверешения работы функции

    def delete(self, key):
        """
        Удаление узла по ключу из всего дерева

        Алгоритм:
        - найти удаляемый узел
        - в зависимости от количества детей:
           - 0 детей: просто удалить ссылку у родителя
           - 1 ребенок: заменить удаляемый узел на его ребенка
           - 2 детей: найти successor (минимальный элемент в правом поддереве) и заменить им удаляемый узел

        Сложность: O(h), где h — высота дерева
        """
        # ищем удаляемый узел
        node = self.search(self.root, key)
        # если узла по такому ключу нет - выходим
        if node is None:
            return None

        # 1 ребенок справа (учитывает и случай, когда удаляемый узел является листом)
        if node.left is None:
            self.replace_subtree(node, node.right)
        # 1 ребенок слева
        elif node.right is None:
            self.replace_subtree(node, node.left)
        # 2 ребенка
        else:
            # берем минимальный узел в правом поддереве, потому что он будет больше всех узлов в текущем левом поддереве,
            # а также меньше всех узлов в текущем правом поддереве
            successor = self.find_min(node.right)
            # если successor не является сразу правым ребёнком удаляемого узла
            if successor.parent != node:
                self.replace_subtree(successor, successor.right)  # правый ребенок (если есть) занимает место successor
                # подвешиваем правое поддерево удаляемого узла к successor
                successor.right = node.right
                successor.right.parent = successor

            self.replace_subtree(node, successor)  # заменяем удаляемый узел на successor
            # подвешиваем левое поддерево удаляемого узла к successor
            successor.left = node.left
            successor.left.parent = successor

        return node

    # ОБХОДЫ ДЕРЕВА:
    # DFS:
    def in_order_traversal(self, runner):
        """
        Симметричный обход (Left -> Runner -> Right)

        Алгоритм: идем влево до конца, потом обрабатываем узел, потом идем вправо до конца

        Пример:
            Дерево:
                    1
                   / \
                  2   3
                 / \ / \
                4  5 6  7
            Inorder (симметричный):
                4 2 5 1 6 3 7

        Сложность: O(n), где n - кол-во узлов
        """
        # если дерево пусто
        if runner is None:
            return []

        result = []
        stack = []

        # если убрать or runner, то правое поддерево последнего узла не будет обработано, если стек к этому моменту пуст
        # условие stack or runner гарантирует, что даже когда стек пуст, но есть ещё узлы для обработки (runner), цикл продолжится
        while stack or runner:
            # если мы не дошли до листа
            if runner:
                stack.append(runner)  # добавляем текущий узел с стек
                runner = runner.left  # идем влево
            # если мы дошли до листа
            else:
                runner = stack.pop()  # извлекаем элемент из стека
                result.append(runner.key)  # сохраняем значение узла
                runner = runner.right  # идем вправо

        return result

    def pre_order_traversal(self, runner):
        """
        Прямой обход (Runner -> Left -> Right)

        Алгоритм: кладем правый узел в стек, потом левый узел в стек, потом достаем верхний и повторяем заново

        Пример:
            Дерево:
                    1
                   / \
                  2   3
                 / \ / \
                4  5 6  7
            Preorder (прямой):
                1 2 4 5 3 6 7

        Сложность: O(n), где n - кол-во узлов
        """
        # если дерево пусто
        if runner is None:
            return []

        result = []
        stack = [runner]  # кладем в стек корень

        # пока просмотрели не все элементы
        while stack:
            runner = stack.pop()  # извлекаем элемент из стека
            result.append(runner.key)  # сохраняем значение узла

            # сначала кладем правого ребенка, потом левого, чтобы левый узел был сверху стека и мы его достали первым

            # если правый ребенок существует
            if runner.right:
                stack.append(runner.right)  # сохраняем правый узел в стек
            # если левый ребенок существует
            if runner.left:
                stack.append(runner.left)  # сохраняем левый узел в стек

        return result

    def post_order_traversal(self, runner):
        """
        Обратный обход (Left -> Right -> Runner)

        Алгоритм: кладем левый узел в стек, потом правый узел в стек, потом достаем верхний и повторяем заново. после разворачиваем полученную цепочку

        Пример:
                Дерево:
                        1
                       / \
                      2   3
                     / \ / \
                    4  5 6  7
                Postorder (обратный):
                    4 5 2 6 7 3 1

        Замечание: post-order - это pre-order, только идем (Runner -> Right -> Left), а затем разворачиваем полученную цепочку

        Сложность: O(n), где n - кол-во узлов
        """
        # если дерево пусто
        if runner is None:
            return []

        result = []
        stack = [runner]  # кладем в стек корень

        # пока просмотрели не все элементы
        while stack:
            runner = stack.pop()  # извлекаем элемент из стека
            result.append(runner.key)  # сохраняем значение узла

            # сначала кладем левого ребенка, потом правого, чтобы правый узел был сверху стека и мы его достали первым

            # если левый ребенок существует
            if runner.left:
                stack.append(runner.left)  # сохраняем левый узел в стек
            # если правый ребенок существует
            if runner.right:
                stack.append(runner.right)  # сохраняем правый узел в стек

        result.reverse()  # разворачиваем полученную цепочку
        return result

    # BFS:
    def level_order_traversal(self, runner):
        """
        Обход по уровням (BFS)
        Пример:
                Дерево:
                        1
                       / \
                      2   3
                     / \ / \
                    4  5 6  7
                Level-order (по уровням):
                    1 2 3 4 5 6 7

        Сложность: O(n), где n - кол-во узлов
        """
        # если дерево пусто
        if runner is None:
            return []

        from collections import deque

        result = []
        queue = deque([runner])  # кладем в очередь корень

        # пока очередь не пуста
        while queue:
            runner = queue.popleft()  # извлекаем элемент из очереди
            result.append(runner.key)  # сохраняем значение узла

            # если левый ребенок существует
            if runner.left:
                queue.append(runner.left)  # сохраняем левый узел в очередь
            # если правый ребенок существует
            if runner.right:
                queue.append(runner.right)  # сохраняем правый узел в очередь

        return result


# Пример использования:
if __name__ == "__main__":
    bst = BinarySearchTree()

    for key in [8, 3, 10, 1, 6]:
        bst.insert(key)

    # Поиск
    node = bst.search(bst.root, 6)
    print("Найденный узел:", node.key)

    # Удаление
    bst.delete(3)
    result_after_delete = []
    bst.range_search(bst.root, 0, 10, result_after_delete)
    print("После удаления 3:", result_after_delete)

"""
Проблема BST:
Если вставлять элементы по порядку:
1 2 3 4 5
дерево становится:
1
 \
  2
   \
    3
     \
      4
высота h = n и сложность становится - O(n)
Это называется вырожденное дерево.

Решение - балансировка.
Идея: дерево должно быть приблизительно сбалансированным.
Идеальный случай: h ≈ log₂ n
пример:
         8
       /  \
      4    12
     / \   / \
    2   6 10 14
Тогда операции: O(log n)
Для балансировки бинарного дерева поиска есть несколько подходов:
1 - AVL-дерево
2 - красно-черное дерево
3 - splay-дерево
4 - декартово дерево
5 - 2-3 дерево
"""
