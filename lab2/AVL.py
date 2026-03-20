class Node:
    def __init__(self, key):
        self.key = key  # значение узла
        self.height = 1  # высота узла
        self.left = None  # ссылка на левого ребенка
        self.right = None  # ссылка на правого ребенка
        self.parent = None  # ссылка на родителя


class AVL:
    def __init__(self):
        self.root = None  # ссылка на корень дерева

    def node_height(self, node):
        """
        Возврат высоты узла node

        Сложность: O(1)
        """
        return node.height if node else 0

    def fix_node_height(self, node):
        """
        Восстановдение корректного значения атрибута height заданного узла
        (при условии, что значения этого поля в правом и левом дочерних узлах являются корректными)

        Сложность: O(1)
        """
        height_left = self.node_height(node.left)  # высота левого поддерева
        height_right = self.node_height(node.right)  # высота правого поддерева

        node.height = max(height_left, height_right) + 1  # обновляем высота поддерева с корнем node

    def balance_factor(self, node):
        """
        Нахождение разности высот поддеревьев узла node

        BF = node_height(right) - node_height(left)

        Дерево сбалансировано, если: BF ∈ {-1, 0, 1}

        Сложность: O(1)
        """
        return self.node_height(node.right) - self.node_height(node.left)

    """
    Обозначения для вращений:
         1. node - текущий корень поддерева
         2. new_root - новый корень после поворота
         3. middle - перебрасываемое поддерево
    """

    def rotate_left(self, node):
        """
        Малое левое вращение

        Пример:
                node                    new_root
               /    \                  /        \
              L   new_root    ->     node        R
                  /      \          /   \       / \
             middle       R        L   middle  M   N
                         / \
                        М   N

        Сложность: O(1)
        """
        new_root = node.right  # правый ребёнок становится новым корнем
        middle = new_root.left  # запоминаем левое поддерево нового корня

        new_root.left = node  # node становится левым ребёнком нового корня
        node.right = middle  # поддерево middle становится правым ребёнком node

        if middle:
            # исправляем родителя middle
            middle.parent = node

        new_root.parent = node.parent  # у нового корня родитель прежний
        node.parent = new_root  # node теперь ребёнок

        self.fix_node_height(node)  # пересчитываем высоту node
        self.fix_node_height(new_root)  # пересчитываем высоту у нового корня

        return new_root  # возвращаем новый корень поддерева

    def rotate_right(self, node):
        """
        Малое правое вращение

        Пример:
                    node                new_root
                   /    \              /        \
              new_root   R    ->      L        node
               /     \               / \      /    \
              L     middle          M   N  middle   R
             / \
            M   N

        Сложность: O(1)
        """
        new_root = node.left  # левый ребёнок становится новым корнем
        middle = new_root.right  # запоминаем правое поддерево нового корня

        new_root.right = node  # node становится правым ребёнком нового корня
        node.left = middle  # поддерево middle становится левым ребёнком node

        if middle:
            # исправляем родителя middle
            middle.parent = node

        new_root.parent = node.parent  # у нового корня родитель прежний
        node.parent = new_root  # node теперь ребёнок

        self.fix_node_height(node)  # пересчитываем высоту node
        self.fix_node_height(new_root)  # пересчитываем высоту у нового корня

        return new_root  # возвращаем новый корень поддерева

    def rebalance(self, node):
        """
        Балансировка произвольного поддерева

        Возвращает новый корень поддерева

        Возможные случаи:
        - BF = 2   -> дерево перекошено вправо
        - BF = -2  -> дерево перекошено влево

        Также проверяем внутренний перекос
        (чтобы определить малое или большое вращение)

        Пример:
            Большое левое вращение:
                node                    node                      C
               /    \                  /    \                   /   \
              L      B     ->         L      C        ->      node   B
                    / \                    /   \             / \    / \
                   C   R                  M     B           L   M  N   R
                  / \                          / \
                 M   N                        N   R
            Большое правое вращение:
                    node                    node                      C
                   /    \                  /    \                   /   \
                  B      R      ->        C      R      ->         B    node
                 / \                     / \                     / \    /   \
                L   C                   B   N                   L   M  N     R
                   / \                 / \
                  M   N               L   M

        Сложность: O(1)
        """
        self.fix_node_height(node)  # обновляем высоту корня поддерева (node)

        BF = self.balance_factor(node)  # считаем баланс-фактор корня поддерева (node)

        # правый перекос
        if BF == 2:
            # случай Right-Left
            if self.balance_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)  # правое вращение

            return self.rotate_left(node)  # левое вращение

        # левый перекос
        if BF == -2:
            # случай Left-Right
            if self.balance_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)  # левое вращение

            return self.rotate_right(node)  # правое вращение

        return node  # если все уже сбалансированно - просто возвращаем узел

    def search(self, runner, key):
        """
        Поиск элемента в дереве

        Сложность: O(log(n)), где n - кол-во узлов
        """
        # пока не дошли до листа поддерева
        while runner:
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
        Вставка элемента в дерево

        Алгоритм:
        - выполняем обычную вставку как в BST
        - поднимаемся вверх по дереву
        - в каждой вершине выполняем балансировку

        Сложность: O(log(n)), где n - кол-во узлов
        """
        new_node = Node(key)  # создаем новый узел

        # если дерево пустое
        if self.root is None:
            # новый узел становится корнем
            self.root = new_node
            return new_node

        runner = self.root  # текущий узел
        parent = None

        # ищем место для вставки

        # идем по дереву
        while runner:
            # запоминаем родителя
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

        # балансировка вверх

        runner = parent  # бегунок, изначально являющийся родителем вставленного узла
        # поднимаемся вверх пока runner не дойдет до корня
        while runner:
            new_root = self.rebalance(runner)  # балансируем поддерево в которое вставили узел

            # если корень поддерева - это корень всего дерева
            if new_root.parent is None:
                self.root = new_root
            # если вращенеи происходило внутри поддерева, а не в корне дерева
            else:
                # если предыдущий (до балансировки) родительский узел был левым ребенком
                if new_root.parent.left == runner:
                    new_root.parent.left = new_root  # исправляем ссылку
                # если предыдущий (до балансировки) родительский узел был правым ребенком
                else:
                    new_root.parent.right = new_root  # исправляем ссылку

            runner = new_root.parent  # поднимаемся дальше

        return new_node  # возвращаем вставленный узел

    def replace_subtree(self, prev, new):
        """
        Замена поддерева prev на поддерево new, сохраняя все связи с родителями

        Сложность: O(1)
        """
        # Если prev - корень дерева, то после замены новый корень становится new
        if prev.parent is None:
            self.root = new
        # Если prev левый ребенок родителя
        elif prev == prev.parent.left:
            prev.parent.left = new  # Родитель prev теперь указывает на new вместо prev
        # Если prev правый ребенок родителя
        else:
            prev.parent.right = new  # Родитель prev теперь указывает на new вместо prev

        # Если new не None, устанавливаем его parent в родителя prev
        if new:
            new.parent = prev.parent

        # Замечание: объект, на который ссылается prev, будет удален GC'ом после заверешения работы функции

    def delete(self, key):
        """
        Удаление узла из дерева

        Алгоритм:
        - находим узел
        - удаляем вершину
        - балансируем дерево вверх

        Сложность: O(log(n)), где n - кол-во узлов
        """
        # ищем удаляемый узел
        delete_node = self.search(self.root, key)
        # если узла по такому ключу нет - выходим
        if delete_node is None:
            return None

        rebalance_start = None  # узел, с которого начнем балансировку после удалени узла

        # если нет левого ребенка (учитывает и случай, когда удаляемый узел является листом)
        if delete_node.left is None:
            rebalance_start = delete_node.parent  # начинаем балансировку с родителя удаляемого узла
            self.replace_subtree(delete_node, delete_node.right)  # заменяем удаляемый узел его правым ребенком

        # если нет правого ребенка
        elif delete_node.right is None:
            rebalance_start = delete_node.parent  # начинаем балансировку с родителя удаляемого узла
            self.replace_subtree(delete_node, delete_node.left)  # заменяем удаляемый узел его левым ребенком

        # если есть два ребенка
        else:
            # берем минимальный узел в правом поддереве, потому что он будет больше всех узлов в текущем левом поддереве,
            # а также меньше всех узлов в текущем правом поддереве
            successor = self.find_min(delete_node.right)
            # если successor не является сразу правым ребёнком удаляемого узла
            if successor.parent != delete_node:
                rebalance_start = successor.parent  # начинаем балансировку с родителя successor'а
                self.replace_subtree(successor, successor.right)  # правый ребенок (если есть) занимает место successor
                # подвешиваем правое поддерево удаляемого узла к successor
                successor.right = delete_node.right
                successor.right.parent = successor
            # если successor является сразу правым ребёнком удаляемого узла
            else:
                rebalance_start = successor  # начинаем балансировку с текущего узла, так как он станет корнем поддерева удаляемого узла

            self.replace_subtree(delete_node, successor)  # заменяем удаляемый узел на successor
            # подвешиваем левое поддерево удаляемого узла к successor
            successor.left = delete_node.left
            successor.left.parent = successor

        # балансировка вверх

        runner = rebalance_start  # бегунок, изначально являющийся узлом стартом баласировки
        # поднимаемся вверх пока runner не дойдет до корня
        while runner:
            new_root = self.rebalance(runner)  # балансируем поддерево в которое вставили узел

            # если корень поддерева - это корень всего дерева
            if new_root.parent is None:
                self.root = new_root
            # если вращенеи происходило внутри поддерева, а не в корне дерева
            else:
                # если предыдущий (до балансировки) родительский узел был левым ребенком
                if new_root.parent.left == runner:
                    new_root.parent.left = new_root  # исправляем ссылку
                # если предыдущий (до балансировки) родительский узел был правым ребенком
                else:
                    new_root.parent.right = new_root  # исправляем ссылку

            runner = new_root.parent  # поднимаемся дальше

        return delete_node  # возвращаем удаленный узел

    def find_min(self, runner):
        """
        Поиск минимума в произвольном поддереве

        Сложность: O(log(n)), где n - кол-во узлов
        """
        # идем до упора влево
        while runner.left:
            runner = runner.left

        return runner  # возвращаем найденный узел

    def find_max(self, runner):
        """
        Поиск максимума в произвольном поддереве

        Сложность: O(log(n)), где n - кол-во узлов
        """
        # идем до упора вправо
        while runner.right:
            runner = runner.right

        return runner  # возвращаем найденный узел

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

    tree = AVL()

    for x in [10, 20, 30, 40, 50, 25]:
        tree.insert(x)

    result = tree.in_order_traversal(tree.root)
    print("AVL:", result)

    tree.delete(40)

    result = tree.in_order_traversal(tree.root)
    print("После удаления:", result)
