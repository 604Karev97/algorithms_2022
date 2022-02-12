"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения.
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import random
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_11(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':
    numbers = [random.randint(1, 100) for _ in range(1000)]

    print(timeit('func_1(numbers)', globals=globals(), number=10000))

    # List comprehension work faster
    print(timeit('func_11(numbers)', globals=globals(), number=10000))
