"""Задание:
Ввести массив целых чисел.
Длина массива задается пользователем.
Определить, упорядочен ли он по возрастанию. По убыванию?"""

def check_input(x):
    while True:
        try:
            check = abs(int(input(x)))
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
    number_input = str(check_input(f'Введите {cycle} элемент: '))
    number_list.extend(number_input)

print('\n')
print(f'Ваш массив {number_list}')

if number_list == sorted(number_list):
    print('Массив отсортирован по возрастанию')

elif number_list == sorted(number_list, reverse=True):
    print('Массив отсортирован по убыванию')
else:
    print('Массив не отсортирован')
exit()
