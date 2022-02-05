"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
import itertools
import random
from typing import TypeVar, Optional, Generic, Iterable, Iterator

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, item: T):
        self.item: T = item
        self.next: Optional[Node[T]] = None

    def set_item(self, item: T):
        self.item = item

    def __str__(self):
        return str(self.item)


class Queue(Generic[T], Iterable):
    """
    Реализация очереди на односвязанном списке.

    Операция вставки нового элемента:    O(1)
    Операция получения первого элемента: O(1)
    Поиск элемента: O(n)
    """

    def __init__(self, items: list[T] = None):
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size = 0

        if items:
            for item in items:
                self.append(item)

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    @property
    def size(self) -> int:
        return self._size

    def append(self, item: T):
        new_node = Node(item)
        self._size += 1

        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def pop(self) -> T:
        if self._size == 0:
            raise ValueError('Queue is empty')

        item = self._head.item

        self._head = self._head.next
        self._size -= 1
        return item

    def __iter__(self):
        node = self._head
        items = []
        while node:
            items.append(node.item)
            node = node.next
        return iter(items)


class TasksDesk(Generic[T]):
    """
    Реализация доски задач.

    есть 3 очереди:
        1) Главная очередь - сюда добавляются новые задачи
        2) Очередь с решенными задачами
        3) Очередь с задачами на доработку


    Если честно не очень понял что конкретно от меня требуется
    """

    def __init__(self):
        self._main: Queue[T] = Queue()
        self._solved: Queue[T] = Queue()
        self._rework: Queue[T] = Queue()

    @property
    def solved(self) -> Iterator[T]:
        return iter(self._solved)

    @property
    def rework(self) -> Iterator[T]:
        return iter(self._rework)

    def append(self, task: T):
        self._main.append(task)

    def start(self):
        """
        Запускаем очередь. Куда отправить задачу (решенные или на доработку)
        определяю рандомно. Задачи разлетаются по разным очередям с вероятностью 50%
        """
        while not self._main.is_empty:
            if random.random() < 0.5:
                self._solved.append(self._main.pop())
            else:
                self._rework.append(self._main.pop())


if __name__ == '__main__':
    queue: Queue[int] = Queue()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)

    assert queue.size == 4

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4

    assert queue.is_empty

    tasks_desk: TasksDesk[int] = TasksDesk()

    tasks_desk.append(1)
    tasks_desk.append(2)
    tasks_desk.append(3)
    tasks_desk.append(4)
    tasks_desk.append(5)

    tasks_desk.start()

    for solved, need_rework in itertools.zip_longest(tasks_desk.solved, tasks_desk.rework):
        print('Solve:', solved)
        print('Rework:', need_rework)

    print('OK')
