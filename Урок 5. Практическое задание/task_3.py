"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует действительности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы, что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы, что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы, что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
from timeit import timeit


def create_deque():
    return deque(range(10000))


def create_list():
    return list(range(10000))


print('Test Append')
print('Append to the list:',
      timeit(
          'l.append(1)',
          setup='l = create_list()',
          globals=globals(), number=10000))
print('Append to the deque:',
      timeit(
          'd.append(1)',
          setup='d = create_deque()',
          globals=globals(), number=10000))

print('Test pop')
print('Pop to the list:',
      timeit(
          'l.pop()',
          setup='l = create_list()',
          globals=globals(), number=10000))
print('Pop to the deque:',
      timeit(
          'd.pop()',
          setup='d = create_deque()',
          globals=globals(), number=10000))

print('Test extend')
print('extend to the list:',
      timeit(
          'l.extend(range(100))',
          setup='l = create_list()',
          globals=globals(), number=10000))
print('extend to the deque:',
      timeit(
          'd.extend(range(100))',
          setup='d = create_deque()',
          globals=globals(), number=10000))

print("""
Вывод: 
Как гласит документация все операции за O(n). Глядя на временные 
замеры можно сказать, что операции не сильно отличается по времени.
""")

print('Test appendleft')
print('appendleft to the list:',
      timeit(
          'l.insert(0, 1)',
          setup='l = create_list()',
          globals=globals(), number=10000))
print('appendleft to the deque:',
      timeit(
          'd.appendleft(1)',
          setup='d = create_deque()',
          globals=globals(), number=10000))

print('Test popleft')
print('popleft to the list:',
      timeit(
          'l.pop(0)',
          setup='l = create_list()',
          globals=globals(), number=10000))
print('popleft to the deque:',
      timeit(
          'd.popleft()',
          setup='d = create_deque()',
          globals=globals(), number=10000))

print('Test extendleft')
print('extendleft to the list:',
      timeit(
          'for _ in range(10): l.insert(0,1)',
          setup='l = create_list()',
          globals=globals(), number=10000))
print('extendleft to the deque:',
      timeit(
          'd.extendleft(range(10))',
          setup='d = create_deque()',
          globals=globals(), number=10000))

print("""
Вывод: 
Что и требовалось ожидать. deque - безусловный победитель по понятный причинам ( при 
добавлении элементов в начало списка, его нужно сдвинуть6 а это дорого)
""")

print('Test get [i]')
print('get middle from the list:',
      timeit(
          'l[len(l) // 2]',
          setup='l = create_list()',
          globals=globals(), number=10000))
print('get middle from the deque:',
      timeit(
          'd[len(d) // 2]',
          setup='d = create_deque()',
          globals=globals(), number=10000))

print("""
Вывод: 
Тут конечно побеждает список, так как для того что бы выцепить 
элемент из дека нужно пробежаться по нему.
""")


if __name__ == '__main__':
    pass
