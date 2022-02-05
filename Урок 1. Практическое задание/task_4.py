"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from collections import namedtuple

UserData = namedtuple('UserData', ['password_hash', 'is_active'])
UserLogin = str


def check_user_data(user_data: UserData, entered_password: str):
    if not user_data.is_active:
        print('This account is not active. Start activation ...')
        user_data.is_active = True
    else:
        if user_data.password_hash == hash(entered_password):
            print('Everything is ok')
        else:
            print('Incorrect password. Try again')


def fast_validate(login: UserLogin, password: str):
    """
    Тут алгоритм будет работать за O(1)
    """
    users_db: dict[UserLogin: UserData] = dict()

    if user_data := users_db.get(login):  # Вот тут добыча значения из словаря это O(1)
        check_user_data(user_data, password)
    else:
        print('User is not authorised. Start authorisation ...')
        users_db[login] = UserData(hash(password), is_active=False)


def slow_validate(login: UserLogin, password: str):
    """
    Этот алгоритм будет работать за O(n)
    """
    users_db: list[tuple[UserLogin, UserData]] = []

    for user_login, user_data in users_db:  # Вот тут проверка на то существует ли пользователь за O(n)
        if user_login == login:
            check_user_data(user_data, password)
    else:
        print('User is not authorised. Start authorisation ...')
        users_db.append((login, UserData(hash(password), is_active=False)))
