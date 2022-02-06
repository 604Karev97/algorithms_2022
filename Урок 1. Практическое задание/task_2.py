"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def fast_min(numbers: list[int]) -> int:
    """
    Сложность этого алгоритма - O(n)
    """
    min_num = None
    for num in numbers:
        if min_num is None:
            min_num = num
        elif num < min_num:
            min_num = num
    return min_num


def dummy_min(numbers: list[int]) -> int:
    """
    Сложность этого алгоритма - O(n^2)
    """
    count = len(numbers)

    # Сортировка пузырьком)
    for i in range(count):
        for j in range(1, count - i):
            if numbers[j - 1] > numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
    return numbers[0]


if __name__ == '__main__':
    lst = [5, 6, 2, 7, 9, 1, 4, 6, 8]

    print('Sorted list', list(sorted(lst)))

    print('min(lst):', min(lst))
    print('fast_min(lst):', fast_min(lst))
    print('dummy_min(lst):', dummy_min(lst))
