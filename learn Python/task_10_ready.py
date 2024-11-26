x = 6                   # начальная точка диапазона
len_range = 10          # конечная точка диапазона включительно
step_range = 4          # шаг диапазона

z = range(x, step_range * (len_range + 1), step_range)      # переменная диапазона

def sum_range(z):
    return sum(z for z in z)


print(f'Сумма всех чисел начиная с {x}, состоящих из {len_range} слагаемых и шагом + {step_range} равна: ' '\n'
      f'{sum_range(z)}')