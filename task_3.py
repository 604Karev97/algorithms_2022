"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from timeit import timeit
from random import randint


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num = str(enter_num)
    return ''.join([enter_num[i] for i in range(len(enter_num)-1, -1, -1)])


some_num = randint(100000, 100000000)
print('Исходное число: ', some_num)

print('Рекурсия')
print(revers_1(some_num))
print(timeit(f'revers_1({some_num})', globals=globals()))

print('Цикл')
print(revers_2(some_num))
print(timeit(f'revers_2({some_num})', globals=globals()))

print('Срезы')
print(revers_3(some_num))
print(timeit(f'revers_3({some_num})', globals=globals()))

print('Мой вариант')
print(revers_4(some_num))
print(timeit(f'revers_4({some_num})', globals=globals()))

'''
Исходное число:  69534333
Рекурсия
33343596.0
9.016976244
Цикл
33343596.0
6.3496479730000015
Срезы
33343596
1.309234923
Мой вариант
33343596
6.467310077999997

Вывод: Рекурсия - самая медленная по исполнению функция из-за наличия арифм. операций.
        Также циклы и моя созданная функция (велосипед реверса) одни из медленных функций (наличие перебора).
        Самая быстрая функция - срезы, так как тут только работа с числом как со строкой.
'''
