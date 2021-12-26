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
from hashlib import sha1


def substring_count(string):
    string = string.lower()
    length = len(string)
    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            if string[i:j] == string:
                pass
            else:
                h = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
                hash_set.add(h)
                print(string[i:j])

    return len(hash_set)


string = input("Введите любое слово: ")
print(f'В слове {string} - {substring_count(string)} подстрок.')
