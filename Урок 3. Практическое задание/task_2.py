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
import sqlite3
import uuid
from hashlib import sha256
from sqlite3 import OperationalError, IntegrityError

con = sqlite3.connect('users.db')
cursor = con.cursor()


def create_users_tabel():
    try:
        cursor.execute("""  
        CREATE TABLE users (
            login TEXT PRIMARY KEY NOT NULL UNIQUE,
            password TEXT NOT NULL,
            salt TEXT NOT NULL
        );""")
        con.commit()
    except OperationalError:
        pass


def add_user(login: str, password: str):
    salt = str(uuid.uuid1())
    password_hash = sha256((password + salt).encode())

    cursor.execute(f"""
    INSERT INTO 
        users 
    VALUES 
        (?, ?, ?);""", (login, password_hash.hexdigest(), salt))

    print(f'Create User({login=}, {password_hash=}, {salt=})')
    con.commit()


def authorize(login: str, password: str):
    for login, password_hash, salt in con.execute('SELECT * FROM users WHERE users.login = ?;', (login,)):
        if sha256((password + salt).encode()).hexdigest() == password_hash:
            print(f'Successfully authorize User with {login=}')
        else:
            print('Authorisation is failed. Check your login and password and try again')


def main():
    create_users_tabel()

    try:
        add_user('user1', 'user1')
        add_user('user2', 'user1')
        add_user('user3', 'user1')
        add_user('user4', 'user1')
    except IntegrityError:
        pass

    # This must be success
    authorize('user2', 'user1')
    authorize('user1', 'user1')

    # This will fail
    authorize('user3', 'qwe')


if __name__ == '__main__':
    main()
