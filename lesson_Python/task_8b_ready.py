
x = range(2, 51, 2)

def sum_range(x):
    return sum(x for x in x)

print(f'Сумма всех чётных чисел от 2 до 50 (включительно) равна: ' '\n'
      f'{sum_range(x)}')
