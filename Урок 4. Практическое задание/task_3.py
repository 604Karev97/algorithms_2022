"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from random import randint
from timeit import timeit


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
    return int(revers_num)


def revers_4(enter_num):
    return int("".join(reversed(str(enter_num))))


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('\nrevers_1')
print(
    timeit(
        "revers_1(num_100)",
        setup='from __main__ import revers_1, num_100',
        number=10000))
print(
    timeit(
        "revers_1(num_1000)",
        setup='from __main__ import revers_1, num_1000',
        number=10000))
print(
    timeit(
        "revers_1(num_10000)",
        setup='from __main__ import revers_1, num_10000',
        number=10000))

print('\nrevers_2')
print(
    timeit(
        "revers_2(num_100)",
        setup='from __main__ import revers_2, num_100',
        number=10000))
print(
    timeit(
        "revers_2(num_1000)",
        setup='from __main__ import revers_2, num_1000',
        number=10000))
print(
    timeit(
        "revers_2(num_10000)",
        setup='from __main__ import revers_2, num_10000',
        number=10000))

print('\nrevers_3')
print(
    timeit(
        "revers_3(num_100)",
        setup='from __main__ import revers_3, num_100',
        number=10000))
print(
    timeit(
        "revers_3(num_1000)",
        setup='from __main__ import revers_3, num_1000',
        number=10000))
print(
    timeit(
        "revers_3(num_10000)",
        setup='from __main__ import revers_3, num_10000',
        number=10000))

print('\nrevers_4')
print(
    timeit(
        "revers_4(num_100)",
        setup='from __main__ import revers_4, num_100',
        number=10000))
print(
    timeit(
        "revers_4(num_1000)",
        setup='from __main__ import revers_4, num_1000',
        number=10000))
print(
    timeit(
        "revers_4(num_10000)",
        setup='from __main__ import revers_4, num_10000',
        number=10000))

if __name__ == '__main__':
    pass
