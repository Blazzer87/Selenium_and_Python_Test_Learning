"""Задание:
Ввести массив целых чисел в диапазоне [-100,100]. Длина массива задается пользователем.
Найти минимальное нечетное
"""


def check_input(x):
    while True:
        try:
            check = int(input(x))
            return check
        except ValueError:
            print('Введены некорректные данные. Давай попробуем снова.')


len_list = check_input('Сколько чисел будет в массиве? (не менее 2-ух):  ')
while len_list <= 1:
    print('Для проверки сортировки массив должен состоять минимум из 2-ух чисел')
    len_list = check_input('Сколько чисел будет в массиве? (не менее 2-ух):  ')

cycle = 0
number_list = list()

while cycle < len_list:
    cycle += 1
    number_input = check_input(f'Введите {cycle} элемент: ')
    while number_input > 100 or number_input < -100:
        print(f'Элемент массива должен быть в диапазоне от -100 до 100')
        number_input = check_input(f'Введите {cycle} элемент: ')
    number_list.extend([number_input])

print('\n')
print(f'Ваш массив {number_list}')

min_number = max(number_list)

for number in range(min(number_list), max(number_list), 1):
    if min_number > number and number % 2 == 1:
        min_number = number

print('\n')
print(f'Минимальный нечётный элемент массива: {min_number} ')
exit()
