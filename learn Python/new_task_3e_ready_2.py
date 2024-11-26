"""Задание:
Ввести массив целых чисел в диапазоне [-100,100]. Длина массива задается пользователем.
Найти минимальный и максимальный элементы и поменять их местами
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
old_number_list = number_list.copy()

min_number = min(number_list)
print(f'Самое маленькое число в массиве = {min_number}')
max_number = max(number_list)
print(f'Самое большое число в массиве = {max_number}')

m = number_list.index(min_number)
n = number_list.index(max_number)

del number_list[m]
number_list.insert(m, max_number)
del number_list[n]
number_list.insert(n, min_number)

print('\n')
print(f'Массив до смены мест {old_number_list}')
print(f'Массив после смены мест {number_list}')


exit()
