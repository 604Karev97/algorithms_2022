"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
from random import randint
import time


def time_of_f(f):
    def wrapped(*args):
        start = time.perf_counter_ns()
        res = f(*args)
        print(time.perf_counter_ns() - start)
        return res

    return wrapped


"""Задание а)"""


@time_of_f
def lst_append():  # O(1)
    return [randint(0, 100) for _ in range(100)]


@time_of_f
def dct_append():  # O(1)
    return {i: randint(0, 100) for i in range(100)}


lst = lst_append()
dct = dct_append()

"""
Запонляется быстрее список, а словарь медленее,
так как для вычисления хешей словаря требуется
больше времени
"""

"""Задание b)"""


@time_of_f
def change_val_lst(lst, old_val, new_val):  # O(1)
    for i in range(len(lst)):
        if lst[i] == old_val:
            lst[i] = new_val


@time_of_f
def change_val_dct(dct, old_val, new_val):  # O(1)
    for val in dct.values():
        if val == old_val:
            val = new_val


@time_of_f
def get_val_lst(lst, i):  # O(1)
    return lst[i]


@time_of_f
def get_val_dct(dct, i):  # O(1)
    return dct[i]


@time_of_f
def del_val_lst(lst, i):  # O(1)
    del lst[i]


@time_of_f
def del_val_dct(dct, i):  # O(1)
    del dct[i]


print('Замена значения в списке')
change_val_lst(lst, 54, 1000)
print('Замена значения в словаре')
change_val_dct(dct, 54, 1000)

"""
Замена значения в словаре происходит быстрее, чем в списке,
так как поиск значение в словаре происходит по его хешу.
"""

print('Получение значения из списка')
print(get_val_lst(lst, 50))
print('Получение значения из словаря')
print(get_val_dct(dct, 50))

"""
Получение значения в словаре происходит происходит примерно 
за такое же время, как и в списке.
"""

print('Удаление значения из списка')
del_val_lst(lst, 60)
print('Удаление значения из словаря')
del_val_dct(dct, 60)

"""
Удаление значения в словаре происходит быстрее, чем в списке,
так как поиск значения в словаре происходит по его хешу.
"""
