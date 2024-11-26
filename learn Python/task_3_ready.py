while True:
    try:
        odd_sum = 0
        cycle = 0
        user_input = str(abs(int(input('Введите число с нечётными цифрами, а я посчитаю их сумму первых трёх: '))))

        while True:
            for n in user_input:
                    if int(n) % 2 == 1:
                        while cycle < 3:
                            odd_sum = odd_sum + int(n)
                            cycle += 1
                            break

            if cycle == 0:
                print("В вашем числе нет ни одной нечётной цифры.")
                break
            elif 0 < cycle < 3:
                print(f'В вашем числе мало нечётных цифр, но я всё равно посчитал их. ' '\n'
                      f'Сумма: {odd_sum}.')
                exit()
            else:
                print(f'Сумма первых трёх нечётных чисел равна:' '\n'
                  f'{odd_sum}')
                exit()

    except ValueError:
        print('Введены не корректные значения.' '\n'
            'Давай попробуем ещё раз')