

while True:
    try:
        fib_1 = 1
        fib_2 = 1
        fib_sum = 0
        fib_next = 0
        cycle = 0

        user_input = abs(int(input('Введи порядковый номер числа Фибоначчи: ')))
        while user_input == 0:
            print(f'Порядковый номер числа Фибоначчи не может быть нулевым')
            user_input = abs(int(input('Введи порядковый номер числа Фибоначчи: ')))

        while cycle < user_input:
            fib_next = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_next
            fib_sum += fib_next - fib_1
            cycle += 1

        print(f'Сумма {user_input} первых чисел Фибоначчи равна: {fib_sum}')
        exit()

    except ValueError:
        print('Введены не корректные значения.' '\n'
              'Давай попробуем ещё раз')