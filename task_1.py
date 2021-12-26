"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i in range(0, len(nums), 2)]


def func_4(nums):
    return list(filter(lambda i: i % 2 == 0, nums))


nums = [i for i in range(100)]

print(func_1(nums))
print(timeit("func_1(nums)", globals=globals(), number=10000))
print(func_2(nums))
print(timeit("func_2(nums)", globals=globals(), number=10000))
print(func_3(nums))
print(timeit("func_3(nums)", globals=globals(), number=10000))
print(func_4(nums))
print(timeit("func_4(nums)", globals=globals(), number=10000))

"""
Вторая функция с LC выполняется быстрее исходной, но третья функция быстрее второй,
так как вместо условия изменяется шаг цикла в LC.
"""
