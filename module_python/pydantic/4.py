from validation_with_typing import Optional

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

"""ПРИМЕР СТАНДАРТНЫЙ"""
class User(BaseModel):
    uuid: str
    name: str
data = """{"uuid": "dickbutt",
        "name": "Gill Bates"}"""
print(User.model_validate_json(data))


"""ПРИМЕР КОГДА ВАЛИДИРУЕТСЯ НЕСТАДАРТНЫЙ ТИП ДАННЫХ, В ДАННОМ СЛУЧАЕ ОБЪЕКТ КЛАССА UUID"""
from uuid import UUID

class User2(BaseModel):
    uuid: UUID
    name: str
data = """{"uuid": "dickbutt",
        "name": "Gill Bates"}"""
User2.model_validate_json(data)       # ВЫДАСТ ООШИБКУ



"""ПРИМЕР КОГДА НЕИЗВЕСТНО ПРИДЁТ ЛИ СПИСОК ИЛИ КОРТЕЖ НО НУЖНО ПРОВАЛИДИРОВАТЬ ИНТ ВНУТРИ НЕГО"""
from validation_with_typing import Sequence

@dataclass
class Bingo:
    numbers: Sequence[int]

seq_list = [1,2,3]
seq_tuple = (1,2,3)
dictionary = {"id":1, "name":"tom"}

for x in seq_list, seq_tuple:
    Bingo(**{'numbers': x})

Bingo(seq_list)         # OK
Bingo(seq_tuple)        # OK
Bingo(dictionary)       # выдаст ошибку


"""ПРИМЕР с UNION когда не знаешь что придёт в данных инт или стринга"""
# from typing import Union
# class User3(BaseModel):
#     any: Union[str, int]                        # объединение двух типов данных
#     name: str
# data_with_str = """{"any": "dickbutt",
#         "name": "Gill Bates"}"""
# data_with_int = """{"any": "dickbutt",
#         "name": "Gill Bates"}"""
# User3.model_validate_json(data_with_str)        # ОК
# User3.model_validate_json(data_with_int)        # ОК



"""ПРИМЕР с чужим ключом"""
# from pydantic import Field
# class User(BaseModel):
#     lastname: str = Field (alias="оченьприоченьдлинныйкакойтоключнафигатакоесоздалинепонятно")
#     name: str
# data = """{"оченьприоченьдлинныйкакойтоключнафигатакоесоздалинепонятно": "Bates",
#         "name": "Gill"}"""
# print(User.model_validate_json(data))


"""ПРИМЕР с декоратором field_validator И АВТОМАТИЧЕСКИМ ВЫЗОВОМ ДЕКОРИРОВАННОЙ ФУНКЦИИ"""
# from pydantic import field_validator
# class User(BaseModel):
#     lastname: str
#     name: str
#
#     @field_validator('lastname')                            # декоратор созданный внутри модельки автоматически проверяет значения
#     def no_lanister_allowed(cls, value: str) -> str:
#         if 'lanister' in value.lower():
#             raise ValueError ('НАЙДЕН ЛАНИСТЕР В ФАМИЛИИ')
#         return value
#
# data_without_lanister = """{"lastname": "Bates",
#         "name": "Gill"}"""
# data_with_lanister = """{"lastname": "lanister",
#         "name": "tirion"}"""
# print(User.model_validate_json(data_without_lanister))      # ОК
# print(User.model_validate_json(data_with_lanister))         # выдаст ошибку



"""ПРИМЕР C МНОЖЕСТВЕННЫМИ УСЛОВИЯМИ ДЛЯ СТРОКИ И ДЛЯ ЧИСЛА"""
# from pydantic import conint, constr, confloat, conlist
# class Guest(BaseModel):
#     age: conint(ge=18, lt=100)
#     name: constr(min_length=2, max_length=20)
#
# John = {"age": 38, "name": "John"}
# print(Guest(**John))                                                       # ОК
# # Guest(age=5, name='Tom')                                                 # ошибка валидации по возрасту
# # Guest(age=21, name='BillyBillyBillyBillyBillyBillyBillyBillyBilly')     # ошибка валидации по длинне имени
#
# class Drink(BaseModel):
#     alc: confloat(ge=0, lt=38)
# vodka = {"alc":10}
# print(Drink(**vodka))       # ОК
# Drink(alc=13.5)             # ОК
# Drink(alc=0)                # ОК
# # Drink(alc=40)               # ошибка валидации по значению
#
# class Party(BaseModel):
#     guest: conlist (item_type=Guest, min_length = 1, max_length = 50)
#     drinks: conlist (item_type=Drink, min_length = 1, max_length = 50)
#
# happy_new_year = {
#                 "guest": [ {"age": 38, "name": "John"}, {"age": 25, "name": "Jack"} ],  # Список с гостями
#                 "drinks": [ {"alc": 10}, {"alc": 30} ]                                   # Список с напитками
#                 }
# print(Party(**happy_new_year))



"""ПРИМЕР C НЕОБЯЗАТЕЛЬНЫМИ УСЛОВИЯМИ И НАСЛЕДОВАНИЕМ"""
# class User(BaseModel):
#     id: int
#     age: Optional[int] = None
#
# class ExtraUser(User):
#     name: str
#
# user = {"id": 123,"name":"Sad"}
# print(ExtraUser(**user))                # ОК
#
# print(ExtraUser(id=123, name="Sad"))    # ОК

