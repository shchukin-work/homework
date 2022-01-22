# Задание 1

with open('test1.txt', 'w') as my_file1:
    while True:
        line = input('Введите текст: ')
        newline = line + '\n'
        my_file1.writelines(newline)
        if not line:
            break
with open('test1.txt', 'r') as my_file1:
    content = my_file1.readlines()
    print(content)

# Задание 2

with open('test2.txt', 'r', encoding="utf-8") as file2:
    my_list = file2.readlines()
    for i in range(len(my_list)):
        new_l = my_list[i].split()
        print(f'Строк в файле - {len(my_list)}. Слов с строке {i + 1} - {len(new_l)}')

# Задание 3

with open('test3.txt', 'r', encoding="utf-8") as workers:
    from statistics import mean
    salaries = []
    for worker in workers:
        last_name, salary = worker.split()
        salary = int(salary)
        if salary < 20000:
            print(last_name)
        salaries.append(salary)
    print(mean(salaries))

# Задание 4

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('test4.txt', 'r', encoding="utf-8") as file_obj:
    content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(content)

with open('test4_1.txt', 'w', encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(content)

# Задание 5

try:
    with open('test5.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел: ')
        file_obj.writelines(line)
        my_numb = line.split()
        print(sum(map(int, my_numb)))
except IOError:
    print('Файл не открывается!')
except ValueError:
    print('Вводите только числа!')

# Задание 6

my_dict = {}
with open("test6.txt", encoding='utf-8') as dict6:
    for line in dict6:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
        my_dict[name] = name_sum
    print(f"{my_dict}")

# Задание 7

with open('test7.txt', 'r+', encoding='utf-8') as file:
    statistics = []
    profit = {}
    average_profit = {}
    av = 0
    prof = 0
    i = 3
    for line in file:
        name, firm, earning, damage = line.split()
        total = int(earning) - int(damage)
        if total >= 0:
            prof = prof + total
        else:
            i -= 1
        profit[name] = total
    statistics.append(profit)
    if i != 0:
        (av) = prof / i
        average_profit['average_profit'] = round(av)
        statistics.append(average_profit)
    else:
        print('У всех фирм отрицательная прибыль')
    print(statistics)

import json

with open('test7_1.json', 'w') as write_js:
    json.dump(statistics, write_js)
    js_str = json.dumps(statistics)
    print(f'Записано в файл test7_1.json: {js_str}')