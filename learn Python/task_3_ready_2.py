
while True:
    try:
        n_number = abs(int(input('Сколько чисел будет введено? ')))
        if n_number < 1:
            print(f'Похоже, что вы ввели {n_number}. Программа будет завершена.')
            exit()

        odd_sum = 0                         # переменная суммы нечётных чисел
        cycle_sum = 0                       # переменная количества циклов суммирования
        cycle_input = 0                     # переменная количества вводов

        while cycle_input < n_number:
            user_number = abs(int(input('Введите число: ')))
            cycle_input += 1
            if user_number % 2 == 1 and cycle_sum < 3:
                odd_sum = odd_sum + user_number
                cycle_sum += 1
                continue

        if cycle_sum == 0:
            print(f'Вы не ввели ни одного нечётного числа, поэтому сумма равна = {odd_sum}')
            exit()
        elif cycle_sum == 1:
            print(f'Вы ввели всего 1 нечётное число, поэтому сумма будет равна введённому числу = {odd_sum}')
            exit()
        elif cycle_sum == 2:
            print(f'Вы ввели 2 нечётных числа, но мне удалось их сложить. Сумма = {odd_sum}')
            exit()
        else:
            print(f'Сумма трёх первых нечётных чисел равна:' '\n'
            f'{odd_sum}')
            exit()

    except ValueError:
        print('Введены некорректные данные. Давай попробуем снова.')

