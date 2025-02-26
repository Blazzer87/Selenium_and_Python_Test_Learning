start_point = 1                 # переменная стартовой точки слагаемых
term = 11                       # количество слагаемых
sum_point = 0                   # сумма числового ряда

while term > 0:
    sum_point = start_point + sum_point
    start_point = start_point + start_point
    term -= 1
print(f'Ответ {sum_point}')

print('второй вариант решения через формулу геометрической прогрессии')

first_num = 1               # первое значение геометрической прогрессии
term = 11                   # количество слагаемых
q = 8 / 4                   # знаменатель прогрессии, отношение следующего значения к предыдущему
sum_progress = 0            # переменная суммы прогрессии


sum_progress = int(first_num*((q ** term)-1)/(q-1))

print(f'Ответ {sum_progress}')