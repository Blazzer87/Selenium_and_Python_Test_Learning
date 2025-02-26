"""
работа с атрибутами класса
"""

class Person:
     name = "Ivan"
     age = 30

print(Person.name)            # Ivan
print(Person.age)            # 30

print(Person.__dict__)            # покажет все атрибуты класса через ДИКТ

print(getattr(Person, 'name'))      # второй вариант получить атрибуты класса через ГЕТАТР
print(getattr(Person, 'age'))

print(getattr(Person, 'surname', 'Vostok'))     # покажи атрибут surname класса Person, и если его не существует то вернётся 3 параметр.
# Помогает избежать исключения AttributeError

Person.name = "Vova"        # изменили атрибут name
print(Person.name)

Person.lastname = "Ivanov"         # при попытке изменить не существующий аттрибут - он создаётся
print(Person.lastname)
print(Person.__dict__)

setattr(Person, 'lastname', 456789)         # изменение атрибута через СЕТАТР
setattr(Person, 'job', 'santehnik')         # создание нового атрибута с присвоением имени через СЕТАТР

print(Person.__dict__)

del Person.job          # удалили атрибут job
print(Person.__dict__)

delattr(Person, "lastname")         # удалили атрибут lastname, вариант 2
print(Person.__dict__)

class Person:
    name = "Ivan"
    age = 30

worker1 = Person()
worker2 = Person()

Person.z = 99999        # экземплярам класса Person автоматически присвоился новый аттрибут Z со значением 99999
print(worker1.z)
print(worker2.z)

del Person.name         # аттрибут name автоматически удалился у всех экземпляров класса Person
