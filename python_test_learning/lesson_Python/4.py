import openpyxl

# Открытие Excel файла
workbook = openpyxl.load_workbook('file.xlsx')

# Выбор активного листа
sheet = workbook.active

# Чтение значений ячеек A1:E1 и создание списка
data = [sheet[f'{col}1'].value for col in ['A', 'B', 'C', 'D', 'E']]

# Вывод списка
print(data)

# Закрытие файла (необязательно, так как openpyxl закрывает его автоматически при выходе из программы)
workbook.close()