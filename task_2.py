"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде.
"""
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    __slots__ = 'value', 'left_child', 'right_child', 'parent'


class BinaryTree:
    def __init__(self, root_obj):
        self.root = Node(root_obj)

    __slots__ = 'root'

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def insert_value(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        # если значение меньше текущего узла - кидаем влево
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
                print(f'Value "{value}" is new left node.')
            else:
                self._insert(value, cur_node.left_child)

        # если значение больше текущего узла - кидаем вправо
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
                print(f'Value "{value}" is new right node.')
            else:
                self._insert(value, cur_node.right_child)

        # если значение совпадает с текущим узлом - вызываем ошибку
        else:
            print(f'Value "{value}" already in tree!')

    @staticmethod
    def get_right_child(cur_node):
        return cur_node.right_child

    @staticmethod
    def get_left_child(cur_node):
        return cur_node.left_child

    def set_root_val(self, obj):
        self.root = Node(obj)

    def get_root_val(self):
        return self.root.value


r = BinaryTree(24)
[r.insert_value(randint(0, 100)) for _ in range(20)]

r.print_tree()

print(r.get_root_val())
r.set_root_val(7)
print(r.get_root_val())


'''
Что я изменил в Вашем коде бинарного дерева:
1. Избавился от надобности валидации путем замены правой и левой вставки на единую функцию insert, а в ней отслеживать,
    вправо или влево пойдет наше текущее значение.
2. Так как работаем с ООП, то добавил слоты для экономии памяти.
3. Добавил сообщения о том, куда было добавлено текущее значение и функцию вывода дерева на консоль.
'''