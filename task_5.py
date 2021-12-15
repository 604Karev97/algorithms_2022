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


class StackClass:
    def __init__(self):
        self.el = [[], [], [], [], []]

    def push_in(self, el):
        for i in range(0, len(self.el) - 1):
            if len(self.el[i]) < 6:
                self.el[i].append(el)
                break

    def pop_out(self):
        return self.el.pop()

    def get_value(self):
        return self.el[len(self.el) - 1]

    def stack_size(self):
        return len(self.el)


class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item


if __name__ == '__main__':
    stack = StackClass()
    for i in range(0, 20):
        stack.push_in(1 + i)

    print(stack.el)
