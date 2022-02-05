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
from operator import itemgetter


def dummy_find(companies: dict[str, float]):
    """
    Сложность алгоритма - O(n * log(n))
    """
    sorted_by_income: list = sorted(companies.items(), key=itemgetter(1))  # O(n * log(n))
    return dict(sorted_by_income[:3])  # O(1)


def fast_find(companies: dict[str, float]):
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
