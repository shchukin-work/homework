# Задание 1

def my_division():
    n1 = float(input('Введите первое число: '))
    n2 = float(input('Введите второе число: '))
    try:
        res = n1 / n2
        print(res)
    except ZeroDivisionError:
        print('Второе число не может быть ноль!')
my_division()

# Задание 2

def face_book (name, surname, year, city, email, phone):
    print('Имя:', name, 'Фамилия:', surname, 'Год рождения:', year,
          'Город проживания:', city, 'E-mail', email, 'Номер телефона', phone)
face_book(name = input('Введите Ваше имя: '),
        surname = input('Введите Вашу фамилию: '),
        year = input('Введите год Вашего рождения: '),
        city = input('Введите город Вашего проживания: '),
        email = input('Введите Ваш e-mail: '),
        phone = input('Введите номер Вашего телефона: '))

# Задание 3

def my_summ(x, y, z):
    print(f'Сумма двух наибольших чисел равна {x + y + z - min([x, y, z])}')
my_summ(
    int(input('Введите число x: ')),
    int(input('Введите число y: ')),
    int(input('Введите число z: ')),
)

# Задание 4

''' Сделал только второй вариант, который без ** '''

def my_exp(a, b):
    b = abs(b)
    for i in range(abs(b - 1)):
        a *= a
    return 1 / a
print(my_exp(3, -2))

# Задание 5

def my_summ2():
    res = 0
    while True:
        user_list = input('Введите числа через пробел, для выхода введите "стоп": ').split()
        for el in user_list:
            if el.lower() == 'стоп':
                print(f'Сумма чисел - {res}')
                return
            else:
                res += int(el)
        print(f'Сумма чисел - {res}')
my_summ2()

# Задание 6

def my_print(text):
    print_list = []
    for i in range(len(text)):
        print_list.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(print_list)
print(my_print(input('Введите несколько слов с латинским строчным написанием, разделенных пробелом: ').split()))

