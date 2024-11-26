

print("Я просуммирую весь нечётный положительный числовой ряд")
user_input = int(input("Введи верхнее ограничение для подсчёта: "))

x = range(1, (user_input + 1), 2)

def sum_range(x):
    return sum(x for x in x)

print(f'Сумма всех нечётных числе от 1 до {user_input} (включительно) равна:' '\n'
      f'{sum_range(x)}')