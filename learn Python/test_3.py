def most_frequent_digit(arr):
    # Создаем словарь для подсчета частоты каждой цифры
    frequency = {}

    # Подсчитываем частоту каждой цифры в массиве
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Инициализируем переменные для хранения максимальной частоты и соответствующей цифры
    max_count = 0
    most_frequent = None

    # Проходим по словарю, чтобы найти цифру с максимальной частотой
    for digit, count in frequency.items():
        # Если текущая частота больше максимальной или равна максимальной, но цифра больше
        if count > max_count or (count == max_count and digit > most_frequent):
            max_count = count
            most_frequent = digit

    return most_frequent, max_count

# Пример использования
arr = [1, 3, 2, 3, 4, 2, 3, 1, 4, 4]
result = most_frequent_digit(arr)
print(f"Цифра: {result[0]}, Количество: {result[1]}")
