"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random


class Game(object):
    def __init__(self, max_attempts: int = 10):
        self._attempts_count = 1
        self._max_attempts = max_attempts
        self._number = random.randint(0, 100)

    def guess(self, num: int):
        if self._attempts_count >= self._max_attempts:
            raise StopIteration()

        if num == self._number:
            print('Победа!!!!')
            return True
        else:
            print(f'Не угадали. Загаданное число {"меньше" if self._number < num else "больше"}.')
            print(f'У вас осталось {self._max_attempts - self._attempts_count} попыток.')
            self._attempts_count += 1
            return False

    def start(self):
        try:
            if not self.guess(int(input('Введите число: '))):
                self.start()
        except StopIteration:
            print('Вы проиграли')


if __name__ == '__main__':
    game = Game()
    game.start()
