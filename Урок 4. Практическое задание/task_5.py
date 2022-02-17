"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (в материалах есть его описание)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
"""
import operator
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def eratosthenes(n):
    """
    Решето эратосфена нужно для поиска простых чисел в диапазоне. Если нужно найти i
    по счету простое число, то перебор делителей - очень хороший вариант
    """
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0

    return filter(lambda prime: prime != 0, sieve)


def prime(i):
    primes, n = [], i
    while len(primes) < i:
        primes = list(eratosthenes(n))
        n += i
    return primes[i - 1]


# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
# print(prime(i))


if __name__ == '__main__':
    number = 100

    """
    Результаты:
    
        1. prime(10)       duration: 0.0013893660070607439
        2. simple(10)      duration: 0.0014435610064538196
        
        1. prime(1000)     duration: 0.6455881490110187
        2. simple(1000)    duration: 25.36205685400637
        
        1. prime(1000)     duration: 0.642583608001587
        2. simple(1000)    duration: 25.252971130990773
    """

    for ind in (10, 1000, 1000):
        times = [
            (f'simple({ind})'.ljust(15), timeit(f'simple({ind})', setup='from __main__ import simple', number=number)),
            (f'prime({ind})'.ljust(15), timeit(f'prime({ind})', setup='from __main__ import prime', number=number)),
        ]

        for i, (f_name, time) in enumerate(sorted(times, key=operator.itemgetter(1))):
            print(f'{i + 1}. {f_name} duration: {time}')
