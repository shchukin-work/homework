# Задание 1

my_list = [123, 'hello', [555, 666, 777], {'город': 'Москва', 'страна': 'Россия'}]
for e in my_list:
    print(f'{e} это {type(e)}')

# Задание 2

user_input = list(input('Введите некоторое значения для формирования списка: '))
for i in range(0, len(user_input)-1, 2):
    user_input[i], user_input[i+1] = user_input[i+1], user_input[i]
print(user_input)

# Задание 3 (решение через словарь)

user_input = int(input('Введите номер месяца (выполняется через словарь): '))
dict = {1: 'Зима',
        2: 'Зима',
        3: 'Весна',
        4: 'Весна',
        5: 'Весна',
        6: 'Лето',
        7: 'Лето',
        8: 'Лето',
        9: 'Осень',
        10: 'Осень',
        11: 'Осень',
        12: 'Зима'}
if user_input in dict:
    print(dict.get(user_input))
else:
    print('Вы не с нашей планеты!')

# Задание 3 (решение через список)

user_input = int(input('Введите номер месяца (выполняется через список): '))
calendar = ['Зима', 'Весна', 'Лето', 'Осень']
if user_input in [1, 2, 12]:
    print(calendar[0])
elif user_input in [3, 4, 5]:
    print(calendar[1])
elif user_input in [6, 7, 8]:
    print(calendar[2])
elif user_input in [9, 10, 11]:
    print(calendar[3])
else:
    print('Вы не с нашей планеты!')

# Задание 4

user_input = input('Введите несколько слов, разделённых пробелами: ').split()
for i, el in enumerate(user_input):
    print(i, el[:9])

# Задание 5

new_el = int(input('Введите новый элемент рейтинга (число): '))
my_list = [7, 5, 3, 3, 2]
all = my_list.count(new_el)
for el in my_list:
    if all > 0:
        i = my_list.index(new_el)
        my_list.insert(i + all, new_el)
        break
    else:
        if new_el > el:
            i = my_list.index(el)
            my_list.insert(i, new_el)
            break
        elif new_el < my_list[len(my_list) - 1]:
            my_list.append(new_el)
print(my_list)

# Задание 6

items = []
i = 0
while True:
    q = input('Добавить новый товар? Введите "да" или "нет": ')
    if q == 'да':
        items.append((int(input('Введите номер порядковый номер товара: ')),
            item_dict({'название': str(input('Введите название товара: ')),
                  'цена': float(input('Введите цену товара: ')),
                  'количество': int(input('Введите количество товара: ')),
                  'eд': input('Введите единцы измерения товара: '),
                }))
                )
    if q == 'нет':
        break
    i += 1
print(f'Список добавленных товаров:{items}')
analitica = item_dict({})
for product in items:
    for key, value in product[-1].items():
        if key in analitica:
            if value not in analitica.get(key):
                analitica.get(key).append(value)
        else:
            analitica.update({key: [value]})
print(f'Собрана аналитика: {analitica}')