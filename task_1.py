"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc


def huffman_encode(s):
    heap = []
    for char, weight in Counter(s).items():
        heap.append((weight, len(heap), Leaf(char)))

    heapq.heapify(heap)

    count = len(heap)
    while len(heap) > 1:
        weight1, _count1, left = heapq.heappop(heap)
        weight2, _count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (weight1 + weight2, count, Node(left, right)))
        count += 1

    code = {}
    if heap:
        [(_weight, _count, root)] = heap
        root.walk(code, "")
    return code


strng = input('Введите любую строку: ')
code = huffman_encode(strng)
encoded = ''.join(code[char] for char in strng)
print(len(code), len(encoded))
for char in sorted(code):
    print(f'{char}: {code[char]}')
print(encoded)
