"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import operator
import random
from collections import Counter
from timeit import timeit

# Увеличил размер массива!
array = [random.randint(1, 100) for _ in range(1000)]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    elem, max_2 = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_4():
    counter = {}
    for elem in array:
        counter[elem] = counter.get(elem, 0) + 1

    elem = max(counter, key=counter.get)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {counter[elem]} раз(а)'


def func_5():
    counter = {}
    m, num = 0, 0
    for elem in array:
        counter[elem] = counter.get(elem, 0) + 1
        if counter[elem] > m:
            m, num = counter[elem], elem

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

number = 100

if __name__ == '__main__':
    times = [
        ('func_1'.ljust(9), timeit("func_1()", setup='from __main__ import func_1', number=number)),
        ('func_2'.ljust(9), timeit("func_2()", setup='from __main__ import func_2', number=number)),
        ('my func_3'.ljust(9), timeit("func_3()", setup='from __main__ import func_3', number=number)),
        ('my func_4'.ljust(9), timeit("func_4()", setup='from __main__ import func_4', number=number)),
        ('my func_5'.ljust(9), timeit("func_5()", setup='from __main__ import func_5', number=number)),
    ]

    for i, (f_name, time) in enumerate(sorted(times, key=operator.itemgetter(1))):
        print(f'{i + 1}. {f_name} duration: {time}')

    # Самый лучший вариант - my func_3
