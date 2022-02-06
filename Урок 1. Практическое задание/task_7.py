"""
Задание 7. На закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром
и в таких строках (включающих пробелы)

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""
from string import punctuation, whitespace


class Deque(object):
    def __init__(self, items: list = None):
        items = items if items else []
        self.items = items

    @property
    def is_empty(self):
        return self.items == []

    def add_right(self, elem):
        self.items.append(elem)

    def add_left(self, elem):
        self.items.insert(0, elem)

    def pop_right(self):
        return self.items.pop()

    def pop_left(self):
        return self.items.pop(0)

    @property
    def size(self):
        return len(self.items)


def clean(string: str):
    """
    Удалим из строки все ненужное
    """
    return string.translate(str.maketrans('', '', punctuation + whitespace))


def pal_checker(string: str):
    deque = Deque(list(clean(string)))

    still_equal = True

    while deque.size > 1 and still_equal:
        still_equal = deque.pop_left() == deque.pop_right()

    return still_equal


if __name__ == '__main__':
    print(pal_checker('q  q'))
    print(pal_checker("молоко делили ледоколом"))
