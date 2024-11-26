
cycle = 0
x = 6
total_sum = 0

while (total_sum + x) < 100:
    total_sum += x
    x += 4
    cycle += 1

print(f'Всего было {cycle} слагаемых и их сумма равна {total_sum}')