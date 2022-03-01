"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from timeit import timeit


def create_arr(length: int):
    return [randint(-100, 99) for _ in range(length)]


arr_10 = create_arr(10)
arr_100 = create_arr(100)
arr_1000 = create_arr(1000)

print('Для len(array) = 10:',
      timeit(
          'statistics.median(arr_10)',
          setup='import statistics',
          globals=globals(), number=1000))
print('Для len(array) = 100:',
      timeit(
          'statistics.median(arr_100)',
          setup='import statistics',
          globals=globals(), number=1000))
print('Для len(array) = 1000:',
      timeit(
          'statistics.median(arr_1000)',
          setup='import statistics',
          globals=globals(), number=1000))

if __name__ == '__main__':
    pass
