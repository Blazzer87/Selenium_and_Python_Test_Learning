"""Задание:
Ввести массив целых чисел в диапазоне [-100,100]. Длина массива задается пользователем.
Найти минимальный и максимальный элементы и поменять их местами
"""

while True:
    try:
        min_input = int(input('Введите МИНимальное значение массива (от -100 до 100 включительно): '))
        while min_input > 100 or min_input < -100:
            print('Ошибка. Введите МИНимальное значение в диапазоне от -100 до 100 (включительно).')
            min_input = int(input('Ещё раз введите МИНимальное значение массива: '))


        max_input = int(input('Введите МАКСимальное значение массива (от -100 до 100 включительно): '))
        while max_input == min_input:
            print('МАКСимальное и МИНимальное значения не могут быть одинаковыми.')
            max_input = int(input('Ещё раз введите МАКСимальное значение массива: '))
        while max_input > 100 or max_input < -100:
            print('Ошибка. Введите МАКСимальное значение в диапазоне от -100 до 100 (включительно).')
            max_input = int(input('Ещё раз введите МАКСимальное значение массива: '))

        if max_input < min_input:
            x = -1
        elif max_input > min_input:
            x = 1

        user_range = range(min_input, max_input + x, x)
        user_list = []

        for z in user_range:
            user_list.append(z)

        old_user_list = user_list.copy()

        min_number = min(user_list)
        print(f'Самое маленькое число в массиве = {min_number}')
        max_number = max(user_list)
        print(f'Самое большое число в массиве = {max_number}')

        m = user_list.index(min_number)
        n = user_list.index(max_number)

        del user_list[m]
        user_list.insert(m, max_number)

        del user_list[n]
        user_list.insert(n, min_number)

        print(f'Массив до смены мест {old_user_list}')
        print(f'Массив после смены мест {user_list}')
        exit()

    except ValueError:
        print('Введены не корректные значения.' '\n'
              'Давай попробуем ещё раз')