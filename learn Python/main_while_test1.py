# присваиваем год
year = 2024
# создаём список/массив с месяцами
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# создаём список/массив с максимальным количеством дней каждом из месяцов в 2024 году
max_month_date = [31,29,31,30,31,30,31,31,30,31,30,31]
# присваиваем число дня, оно будет обнуляться с началом нового месяца
day_number = 1
# присваиваем счётчик дней, он будет прирастать в течение всего года
day_count = 0
# создаём переменную
var = 0

# выводим Календарь и год
print('Календарь', year)
# выводим название месяца, 0 индекс
print(month[var])

try:
    # запускаем основной цикл генерации месяцев
    while day_count <= 366:
        # запускаем вложенный цикл, который длится пока номер/число дня меньше суммы максимальных дат за прошедшие месяцы
        while day_number <= max_month_date[var]:
        # выводим печать понедельно, чтобы каждая новая неделя начиналась с верной даты
            if day_count % 7 == 0 and day_count > 1:
            # делаем перенос на новую строку
                print('\n')
        # выводим дату и делаем отступы между датами
            print(day_number, end='\t')
        # приращиваем счётчик дней
            day_count += 1
        # приращиваем дату +1 к каждому циклу внутри месяца
            day_number += 1
        # делаем перенос на новую строку
        print('\n')
        # приращиваем переменную подсчёта месяцев
        var += 1
        # выводим название следующего месяца
        print(month[var])
        # сбрасываем дату месяца для начала нового цикла
        day_number = 1
        # добавляем переменную которая регулирует положение дня в цикле одной недели
        # и показывает необходимое кол-во пробелов
        shift = day_count % 7
        # создаём цикл на создание пробелов для корректного отображения 1 числа месяца в рамках недели
        while shift > 0:
            print(end='\t')
            shift -= 1

except IndexError:
    print('Работа календаря выполнена')