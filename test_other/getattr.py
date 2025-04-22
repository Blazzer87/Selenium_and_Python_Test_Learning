class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Создаем объект класса Person
person = Person("Alice", 30)

# Получаем атрибуты с помощью getattr
name = getattr(person, 'name')  # Получаем значение атрибута 'name'
age = getattr(person, 'age')     # Получаем значение атрибута 'age'

print(name)  # Вывод: Alice
print(age)   # Вывод: 30


print(person.name)



# Попробуем получить несуществующий атрибут
address = getattr(person, 'address', 'Unknown')  # Указываем значение по умолчанию
print(address)  # Вывод: Unknown


