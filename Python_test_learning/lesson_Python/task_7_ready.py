while True:
    try:
        x = 0
        text_len = 1
        space = ' '
        text = '*'

        n = abs(int(input('Введите числовое значение стороны ромба "n" = ')))
        while n == 0:
            print('Число "n" не соответствует условиям')
            n = abs(int(input('Введите числовое значение стороны ромба "n" = ')))

        print ('Рисуем ромб')
        space_len = int(n)
        while x < n:
            print(space * space_len, text * text_len, space * space_len)
            x += 1
            space_len -= 1
            text_len += 2
        x = 0
        text_len -= 4
        space_len += 2
        while x < n:
            print(space * space_len, text * text_len, space * space_len)
            x += 1
            space_len += 1
            text_len -= 2
        print(f'Это ромб со стороной {n} ')
        exit()


    except ValueError:
        print('Введены не корректные значения.' '\n'
            'Давай попробуем ещё раз')



