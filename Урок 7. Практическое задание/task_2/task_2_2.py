"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint, choice
from timeit import timeit


def median(array: list[int]):
    return quickselect(array, len(array) / 2)


def quickselect(array, k):
    if len(array) == 1:
        return array[0]

    pivot = choice(array)

    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def create_arr(length: int):
    return [randint(-100, 99) for _ in range(length)]


arr_10 = create_arr(10)
arr_100 = create_arr(100)
arr_1000 = create_arr(1000)

print('Для len(array) = 10:',
      timeit(
          'median(arr_10)',
          globals=globals(), number=1000))
print('Для len(array) = 100:',
      timeit(
          'median(arr_100)',
          globals=globals(), number=1000))
print('Для len(array) = 1000:',
      timeit(
          'median(arr_1000)',
          globals=globals(), number=1000))

if __name__ == '__main__':
    pass
