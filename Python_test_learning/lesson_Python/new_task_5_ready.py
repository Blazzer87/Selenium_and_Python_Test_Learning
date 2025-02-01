"""Задание:
Считать из файла массив целых чисел. Упорядочить по возрастанию.
Вывести обратно в файл."""


with open('new_task_list_5.txt', 'r') as file:
    num = file.readline()

number_list = []
for n in num:
    if n == '\n':
        break
    number_list.append(int(n))

number_list_sort = sorted(number_list)

print(f'Массив до сортировки: {number_list}')
print(f'Массив после сортировки: {number_list_sort}')

with open('new_task_list_5.txt', 'a') as file:
    file.write('\n')
    file.write(str(number_list_sort))

