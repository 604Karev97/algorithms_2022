"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
from hashlib import md5
from itertools import combinations


def count_substrings(string: str):
    substrings = [string[x:y] for x, y in combinations(range(len(string) + 1), r=2)]
    hashes = {md5(s.encode()).hexdigest() for s in substrings}
    print(f'String {string} contains {len(hashes) - 1} unique substrings')
    return len(substrings) - 1


if __name__ == '__main__':
    assert count_substrings('рара') == 6
