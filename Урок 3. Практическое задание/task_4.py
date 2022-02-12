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
from hashlib import sha256


class WebHasher(object):
    def __init__(self):
        self.__statis_salt = '44b2aaeb4309f9739481611b46ab035c370de165d164fc3873eb845aa3794c91'
        self.__hashed_sites = {}

    def get_hash(self, url: str):
        return self.__hashed_sites.setdefault(url, sha256(f'{url}{self.__statis_salt}'.encode()))


if __name__ == '__main__':
    hasher = WebHasher()

    print(hasher.get_hash('http://localhost:5000').hexdigest())
