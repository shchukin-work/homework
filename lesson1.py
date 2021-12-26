# Задание 1

age = 18
city = 'Москва'
print(f'Возраст - {age}, город - {city}')

number = int(input('Введите число от 1 до 10: '))
os = input('Введите название Вашей операционной системы: ')
print(f'Вы ввели число {number}, Ваша ОС - {os}')

car = int(input('Введите год выпуска Вашего автомобиля: '))
car_model = input('Введите марку и модель Вашего автомобиля: ')
print(f'У Вас {car_model} {car} года выпуска')

# Задание 2

input_time = int(input('Введите время в секундах: '))
time_hour = input_time // 3600
time_min = input_time % 3600 // 60
time_sec = input_time % 60
print(f'Время в формате "чч:мм:сс": {time_hour}:{time_min}:{time_sec}')

# Задание 3

n = int(input('Введите число n: '))
n_str = str(n)
nn = n_str*2
nnn = n_str*3
result = n + int(nn) + int(nnn)
print(f'n+nn+nnn={result}')

# Задание 4

n = int(input('Введите целое положительное число: '))
last_n = n % 10 # последняя цифра числа (если n = 56721, то last_n = 1)
n = n // 10 # "новое" число (если изначально n = 56721, то уже эта n = 5672)
while n > 0:
    if n % 10 > last_n: # 5672 % 10 = 2, 2 > 1?
        last_n = n % 10 # 1 = 5672 % 10 = 2
    n = n // 10 # 5672 = 5672 // 10 = 567
print(f'Наибольшая цифра в числе - {last_n}')

# Задание 5

proceed = int(input("Введите выручку Вашей фирмы: "))
outlay = int(input("Введите издержки Вашей фирмы: "))
if proceed > outlay:
    profit = proceed-outlay
    rent = profit/proceed
    print(f"Поздравляем, Ваш доход {profit}. Рентабельность {rent}")
    workers = int(input("Сколько человек работает в Вашей фирме: "))
    for_one = int(profit/workers)
    print(f"{for_one} - прибыль фирмы на одного сотрудника")
elif proceed == outlay:
    print("Поднажмите!")
else:
    print("Вы отличный стратег!")

# Задание 6

a = float(input("Результат в километрах на сегодняшний день: "))
b = float(input("Планируемый результат в километрах: "))
day = 1
if a > b:
    print('Вы выполнили план!')
while a < b:
    a = a + a/10
    day += 1
print(f'Для достижение планируемого результата Вам поднадобится {day} дней.')
