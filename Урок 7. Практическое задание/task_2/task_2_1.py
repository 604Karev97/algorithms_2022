"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def gnome_sort(array: list[int]):
    array = array.copy()
    i, size = 1, len(array)
    while i < size:
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array


def get_med(array: list[int]):
    return gnome_sort(array)[len(array) // 2]


# тесты
arr = [1, 2, 4, 5, 3, 2, 6]

assert gnome_sort(arr) == [1, 2, 2, 3, 4, 5, 6]
assert get_med(arr) == 3


# замеры
def create_arr(length: int):
    return [randint(-100, 99) for _ in range(length)]


arr_10 = create_arr(10)
arr_100 = create_arr(100)
arr_1000 = create_arr(1000)

print('Для len(array) = 10:',
      timeit(
          'get_med(arr_10)',
          globals=globals(), number=100))
print('Для len(array) = 100:',
      timeit(
          'get_med(arr_100)',
          globals=globals(), number=100))
print('Для len(array) = 1000:',
      timeit(
          'get_med(arr_1000)',
          globals=globals(), number=100))

if __name__ == '__main__':
    pass
