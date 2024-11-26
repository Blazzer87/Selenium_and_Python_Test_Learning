"""Задание:
Ввести два упорядоченных массива (контроль за корректностью ввода).
Слить их в один упорядоченный массив без использования сортировки."""

def check_input(x):
    while True:
        try:
            check = str(abs(int(input(x))))
            return check
        except ValueError:
            print('Введены некорректные данные. Давай попробуем снова.')

number_input_1 = check_input('Введите отсортированный 1-ый массив : ')
number_list_1 = []
number_list_1.extend(number_input_1)
number_list_1_int = list(map(int, number_list_1))

while number_list_1_int != sorted(number_list_1_int) and number_list_1_int != sorted(number_list_1_int, reverse=True):
    print('Ваш массив не отсортирован, программа не может быть выполнена.')
    number_input_1 = check_input('Введите отсортированный 1-ый массив : ')
    number_list_1 = []
    number_list_1.extend(number_input_1)
    number_list_1_int = list(map(int, number_list_1))

if number_list_1_int == sorted(number_list_1_int):
    rev1 = False
elif number_list_1_int == sorted(number_list_1_int, reverse=True):
    rev1 = True

number_input_2 = check_input('Введите отсортированный 2-ой массив : ')
number_list_2 = []
number_list_2.extend(number_input_2)
number_list_2_int = list(map(int, number_list_2))

while number_list_2_int != sorted(number_list_2_int) and number_list_2_int != sorted(number_list_2_int, reverse=True):
    print('Ваш массив не отсортирован, программа не может быть выполнена.')
    number_input_2 = check_input('Ещё раз введите отсортированный 2-ой массив : ')
    number_list_2 = []
    number_list_2.extend(number_input_2)
    number_list_2_int = list(map(int, number_list_2))

if number_list_2_int == sorted(number_list_2_int):
    rev2 = False
elif number_list_2_int == sorted(number_list_2_int, reverse=True):
    rev2 = True

if rev1 != rev2:
    print('Ваш 2-ой массив имеет сортировку, отличающуюся от сортировки 1-го массива.' '\n'
          'По умолчанию, к итоговому массиву будет применён тот вид сортировки, который был у 1-го массива.' '\n')

number_list_sum = number_list_1_int + number_list_2_int
final_list = []

if number_list_1_int == sorted(number_list_1_int):
    for num_range in range(min(number_list_sum), max(number_list_sum) + 1):
        for index, num_list in enumerate(number_list_sum):
            if num_range == num_list:
                final_list.append(num_range)
if number_list_1_int == sorted(number_list_1_int, reverse=True):
    for num_range in range(max(number_list_sum), min(number_list_sum) - 1, -1):
        for index, num_list in enumerate(number_list_sum):
            if num_range == num_list:
                final_list.append(num_range)

print(f'Полученный массив: {final_list}')










