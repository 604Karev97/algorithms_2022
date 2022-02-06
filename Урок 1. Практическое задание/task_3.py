"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
import random
import time
from operator import itemgetter
from typing import Callable


def profile(f: Callable):
    def wrapper(*args, **kwargs):
        t_start = time.time()
        f(*args, **kwargs)
        print(f'{f.__name__} отработала за {time.time() - t_start}')

    return wrapper


@profile
def fast_find(companies: dict[str, float]):
    """
    Сложность алгоритма - O(n * log(n))
    """
    sorted_by_income: list = sorted(companies.items(), key=itemgetter(1))  # O(n * log(n))
    return dict(sorted_by_income[:3])  # O(1)


@profile
def dummy_find(companies: dict[str, float]):
    """
    Сложность алгоритма - O(n)
    """
    the_most_successful: list[tuple[str, float]] = []
    for comp, income in companies.items():  # O(n)
        if len(the_most_successful) < 3:  # O(1)
            the_most_successful.append((comp, income))  # O(1)
            continue  # O(1)

        the_most_successful.sort(key=itemgetter(1), reverse=True)  # O(1)
        if income > the_most_successful[0][1]:  # O(1)
            the_most_successful.pop()  # O(1) так как достаем с конца
            the_most_successful.append((comp, income))  # O(1)

    return dict(the_most_successful)  # O(1)


def generate_companies(n: int) -> dict:
    return {f'company{i}': round(random.random(), 4) * 1000 for i in range(n)}


if __name__ == '__main__':
    _companies = generate_companies(100000)

    dummy_find(_companies)
    fast_find(_companies)
