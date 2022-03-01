"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
import random
from timeit import timeit


def optimized_bubble_sort(arr: list[int]):
    sort_arr = arr.copy()
    for i in range(len(sort_arr)):
        num_of_swaps = 0
        for j in range(1, len(sort_arr) - i):
            if sort_arr[j - 1] < sort_arr[j]:
                num_of_swaps += 1
                sort_arr[j - 1], sort_arr[j] = sort_arr[j], sort_arr[j - 1]
        if num_of_swaps == 0:
            break
    return sort_arr


def bubble_sort(arr: list[int]):
    sort_arr = arr.copy()
    for i in range(len(sort_arr)):
        for j in range(1, len(sort_arr) - i):
            if sort_arr[j - 1] < sort_arr[j]:
                sort_arr[j - 1], sort_arr[j] = sort_arr[j], sort_arr[j - 1]
    return sort_arr


test_array = [1, 3, 4, 5, 1]

# тесты
assert bubble_sort(test_array) == [5, 4, 3, 1, 1]
assert optimized_bubble_sort(test_array) == [5, 4, 3, 1, 1]

array = [random.randint(-100, 100 - 1) for _ in range(1000)]

print('Массив:', array)
print('отсортированный массив:', optimized_bubble_sort(array))

print('Замеры реализаций')

print('Для оптимизированной сортировки пузырьком:',
      timeit(
          'optimized_bubble_sort(array)',
          globals=globals(), number=10))
print('Для НЕ оптимизированной сортировки пузырьком:',
      timeit(
          'bubble_sort(array)',
          globals=globals(), number=10))

print()
print()
print()
print('''
Вывод: оптимизированный вариант работает хуже. Так как ситуация, в котрой мы не будет делать перестановки очень редко 
встречается при рандомной генерации массива. Но есть на вход обоим алгоритмам передать уже отсортированный массив, то
оптимизированный алгоритм отработает гораздо быстрее.
''')

if __name__ == '__main__':
    pass
