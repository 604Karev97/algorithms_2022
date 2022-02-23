"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from __future__ import annotations


def mul_xec(a: tuple[str, ...], b: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(format(int(''.join(a), 16) * int(''.join(b), 16), 'X'))


def add_xec(a: tuple[str, ...], b: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(format(int(''.join(a), 16) + int(''.join(b), 16), 'X'))


class XecNum(object):
    def __init__(self, num: str):
        self._dig = tuple(num.upper())

    def __mul__(self, other: XecNum):
        return mul_xec(self._dig, other._dig)

    def __add__(self, other: XecNum):
        return add_xec(self._dig, other._dig)


if __name__ == '__main__':
    assert add_xec(('A', '2'), ('C', '4', 'F')) == ('C', 'F', '1')
    assert mul_xec(('A', '2'), ('C', '4', 'F')) == ('7', 'C', '9', 'F', 'E')

    a = XecNum('A2')
    b = XecNum('C4f')

    assert a + b == ('C', 'F', '1')
    assert a * b == ('7', 'C', '9', 'F', 'E')
