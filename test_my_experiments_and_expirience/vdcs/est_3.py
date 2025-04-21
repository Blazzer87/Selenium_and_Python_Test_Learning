import re

data = 'pmi-kind6'

# Используем D для удаления всех нецифровых символов
newdata = int(re.sub(r'[a-zA-Z_-]', '', data)) + 1

print(newdata)  # Вывод: 526
