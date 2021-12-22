"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

from hashlib import pbkdf2_hmac
from binascii import hexlify

cash_dct = {}


def chek_url(url):
    hash_url = pbkdf2_hmac(hash_name='sha512',
                           password=url.encode('utf-8'),
                           salt=b'salt_for_url',
                           iterations=1000)
    res_hash = hexlify(hash_url)
    if res_hash in cash_dct.keys():
        return True
    else:
        return {res_hash: url}


while True:
    url = input('Введите URL: ')
    if url == '0':
        exit()

    chek_url(url)

    try:
        cash_dct.update(chek_url(url))
    except TypeError:
        print("Такой объект уже есть в кэше")

    print(cash_dct)
