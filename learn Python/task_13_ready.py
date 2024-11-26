
x = 6                   # начальная точка диапазона
y = 100                 # конечная точка диапазона включительно
z = range(x, y, 4)

def sum_range(z):
    return sum(z for z in z)


def len_range(z):
    return len(z)


print(f'Сумма всех чисел диапазона от {x} до {y} (включительно) с шагом +4 равна: ' '\n'
      f'{sum_range(z)}' '\n'
      f'Длинна суммируемого диапазона равна: ' '\n'
      f'{len_range(z)}')