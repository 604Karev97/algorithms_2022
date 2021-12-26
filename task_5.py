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


def sieve(n):
    length = n ** 2
    simple_nums = [el for el in range(length)]
    simple_nums[1] = 0
    i = 2

    while i < length:
        if simple_nums[i] != 0:
            j = i * 2

            while j < length:
                simple_nums[j] = 0
                j += i
        i += 1
    return [el for el in simple_nums if el != 0][n - 1]


print(timeit(f"simple({10})", globals=globals(), number=10))
print(timeit(f"sieve({10})", globals=globals(), number=10))

print(timeit(f"simple({100})", globals=globals(), number=10))
print(timeit(f"sieve({100})", globals=globals(), number=10))

print(timeit(f"simple({1000})", globals=globals(), number=10))
print(timeit(f"sieve({1000})", globals=globals(), number=10))

print(timeit(f"simple({10000})", globals=globals(), number=10))
print(timeit(f"sieve({10000})", globals=globals(), number=10))

# Диапазон до 10 за 10 замеров.
# 0.0006914700000000273
# 0.001045070999999953

# Диапазон до 100 за 10 замеров.
# 0.07902868600000001
# 0.14958258799999996

# Диапазон до 1000 за 10 замеров.
# 12.721040666
# 18.326689246
