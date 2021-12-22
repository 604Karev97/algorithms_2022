"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

from hashlib import pbkdf2_hmac
from binascii import hexlify
import csv


def create_hash(login, password):
    hash_pass = pbkdf2_hmac(hash_name='sha256',
                            password=password.encode('utf-8'),
                            salt=login.encode('utf-8'),
                            iterations=1000)
    res_pass = hexlify(hash_pass)
    return res_pass


def verify_password(login, password):
    hash_pass = create_hash(login, password)

    with open('data.csv', 'r') as f_read:
        reader = csv.reader(f_read, delimiter=',')
        for row in reader:
            if str(hash_pass) in row:
                print('Вы вошли в систему.')
                exit()
        with open('data.csv', 'a') as f_append:
            appender = csv.writer(f_append, delimiter=',', lineterminator="\r")
            appender.writerow([login, hash_pass])
            print('Запись добавлена.')


while True:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    verify_password(login, password)
