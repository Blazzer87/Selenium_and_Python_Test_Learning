
x = range(1, 51)

def sum_range(x):
    return sum(x for x in x)

print(f'Сумма всех чисел от 1 до 50 (включительно) равна: ' '\n'
      f'{sum_range(x)}')