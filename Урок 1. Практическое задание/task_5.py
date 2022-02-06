"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""
from functools import reduce


class Stack(object):
    def __init__(self, items: list = None):
        if items:
            self._items = items
        else:
            self._items = []

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self._items)

    def pop(self):
        if self.size == 0:
            return None
        return self._items.pop()

    def append(self, item):
        self._items.append(item)


class BalancedStack(Stack):
    def __init__(self, max_size: int, items: list = None):
        super().__init__([Stack()])
        self._max_size = max_size

        items = items if items else []
        for item in items:
            self.append(item)

    @property
    def size(self):
        return reduce(lambda prev, stack: prev + stack.size, self._items, 0)

    @property
    def num_of_sub_stacks(self):
        return super().size

    def pop(self):
        if self.size == 0:
            return None

        # Достанем последний стек
        last_stack: Stack = self._items[-1]

        # Если в стеке есть элемент, то вернем его.
        # Иначе повторим операцию
        if last_elem := last_stack.pop():
            return last_elem

        # Удалим пустой дочерний стек
        self._items.pop()
        return self.pop()

    def append(self, item):
        last_stack: Stack = self._items[0]

        if last_stack.size == self._max_size:
            new_stack = Stack([item])
            self._items.append(new_stack)
        else:
            return last_stack.append(item)


if __name__ == '__main__':
    _stack = Stack([1, 2, 3])

    assert _stack.size == 3
    assert _stack.pop() == 3
    assert _stack.pop() == 2
    assert _stack.pop() == 1
    assert _stack.is_empty

    _stack.append(1)
    assert _stack.pop() == 1

    _stack = BalancedStack(3)

    _stack.append(1)
    _stack.append(2)
    _stack.append(3)
    _stack.append(4)

    assert _stack.size == 4
    assert _stack.num_of_sub_stacks == 2

    assert _stack.pop() == 4
    assert _stack.pop() == 3
    assert _stack.pop() == 2
    assert _stack.pop() == 1

    assert _stack.is_empty
