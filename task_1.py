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
    lst = []
    for i in range(100):
        lst.append(randint(0, 100))
    return lst


@time_of_f
def dct_append():  # O(1)
    dct = {}
    for i in range(100):
        dct[i] = randint(0, 100)
    return dct


lst = lst_append()
dct = dct_append()

"""
Запонляется быстрее словарь, так как является хеш-таблицей, 
но занимает больше места в памяти, чем список
"""

"""Задание b)"""


@time_of_f
def change_val_lst(lst, old_val, new_val):  # O(1)
    for i in range(len(lst)):
        if lst[i] == old_val:
            lst[i] = new_val


@time_of_f
def change_val_dct(dct, old_val, new_val):  # O(1)
    for i in range(len(dct)):
        if dct[i] == old_val:
            dct[i] = new_val


@time_of_f
def get_val_lst(lst, i):  # O(1)
    return lst[i]


@time_of_f
def get_val_dct(dct, i):  # O(1)
    return dct[i]


@time_of_f
def del_val_lst(lst, i):  # O(1)
    lst.pop(i)


@time_of_f
def del_val_dct(dct, i):  # O(1)
    dct.pop(i)


print('Замена значения в списке')
change_val_lst(lst, 54, 1000)
print('Замена значения в словаре')
change_val_dct(dct, 54, 1000)

print('Получение значения из списка')
print(get_val_lst(lst, 50))
print('Получение значения из словаря')
print(get_val_dct(dct, 50))

print('Удаление значения из списка')
del_val_lst(lst, 60)
print('Удаление значения из словаря')
del_val_dct(dct, 60)

"""
По данным замеров времени в программе: поиск, замена, 
получение и удаление значения в списке проходит быстрее, чем в словаре
"""
