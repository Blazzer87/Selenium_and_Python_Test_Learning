
x = 6                   # начальная точка диапазона
y = 46                  # конечная точка диапазона включительно
step = 4

z = range(x, y + 1, step)

def sum_range(z):
    return sum(z for z in z)

def len_range(z):
    return len(z)

print(f'Сумма всех чисел от {x} до {y} (включительно) с шагом + {step} равна: ' '\n'
      f'{sum_range(z)}' '\n'
      f'Длинна суммируемого диапазона равна: ' '\n'
      f'{len_range(z)}')
