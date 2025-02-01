""" Функция как атрибут класса"""

class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod                   # декоратор статикметод избавляет от ошибки
    def drive():
        print("LETS GO")

Car.drive()                      # вызов функции которая выведет LETS GO
getattr(Car, 'drive')()          # второй вариант вызова функции LETS GO, в конце обязательно ()!!!

auto1 = Car()                   # создадим объект класса

auto1.drive()                   # вызовем функцию атрибута класса через экземпляр, НО ПОЛУЧИМ ОШИБКУ ПОТОМУ ЧТО НИЧЕГО НЕ ПЕРЕДАЛИ В ФУНКЦИЮ - Car.drive() takes 0 positional arguments but 1 was given