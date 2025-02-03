"""
магическиая функция __str__ опеределяет представление объекта x класса Number
"""
class Number:


    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def sum (self, other):
        self.num = self.num + other


x = Number(5)
print(x)

x.sum(3)
print(x)

y = 5
print(type(x))  # объект создан как объект класса Number
print(type(y))  # объект создан не от класса поэтому имеет тип интеджер