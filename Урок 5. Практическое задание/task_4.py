"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


# В версии после 3.6 словари сохраняют порядок, так что необходимости в OrderedDict нет

def create_dict():
    return dict(tuple(enumerate(range(10000))))


def create_ordereddict():
    return OrderedDict(tuple(enumerate(range(10000))))


print('Test equals')
print('get middle from the list:',
      timeit(
          'd1 = d2',
          setup='d1 = create_dict(); d2 = create_dict()',
          globals=globals()))
print('get middle from the deque:',
      timeit(
          'd1 = d1',
          setup='d1 = create_ordereddict(); d2 = create_ordereddict()',
          globals=globals()))

print('Test get')
print('get last from dict:',
      timeit(
          'd.get(len(d))',
          setup='d = create_dict()',
          globals=globals()))
print('get last from OrderedDict:',
      timeit(
          'd.get(len(d))',
          setup='d = create_ordereddict()',
          globals=globals()))

print("""
Вывод: 
Никакой разницы. Разве, что dict совсем чуточку быстрее.
""")

if __name__ == '__main__':
    pass
