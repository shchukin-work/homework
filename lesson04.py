# Задание 1 (передаем параметры в терминале)

from sys import argv
p1, p2, p3 = map(int, argv[1:])
print(p1 * p2 + p3)

# Задание 2

list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(new_list)

# Задание 3

list_2 = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(list_2)

# Задание 4

list_3 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list_3 = [el for el in list_3 if list_3.count(el)==1]
print(new_list_3)

# Задание 5

from functools import reduce
list_4 = [i for i in range(100, 1001, 2)]
print(reduce(lambda a,b: a*b, list_4))

# Задание 6 (итератор 1)

from itertools import count
for i in count(int(input("Введите целое число до 10:"))):
    print(i)
    if i == 10:
        break

# Задание 6 (итератор 2)

from itertools import cycle
j = 0
for i in cycle([11, 222, 3333]):
    print(i)
    j += 1
    if j == 9:
        break

# Задание 7

from math import factorial

def fact(n):
    for i in range(n):
        print(i, end=' - число, его факториал = ')
        yield factorial(i)
for el in fact(5):
    print(el)