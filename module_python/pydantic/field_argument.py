
from datetime import date
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field, condecimal


class User(BaseModel):
    id: int = Field(frozen=True)
    # фиксирует значение атрибута у экземпляра, попытка изменить его вызовет исключение AttributeError

    name: str = Field(alias='firstname')
    # управляет входящим неймингом полей из чужих данных

    age: int = Field(strict=True)
    # если истина то включает строгий режим типизации, теперь "37" не переведётся в int самостоятельно

    lastname: str = Field(title="этот тайтл не влияет на валидацию, а используется только для читаемости кода")

    birthday_date: date = Field(repr=False)
    # убирает из вывода через функцию repr если = false

    password: str = Field(exclude=True)
    # исключает из сериализации, у экземпляра будет этот атрибут, но его не будет в строке или словаре, может также быть использовано с model_dump() и model_dump_json()

    tel: int = Field(default="+79507586687", validate_default=True)
    # если аргумент отсутствует в данных при создании экземпляра, то дефолтное значение будет передано по умолчания. Если передано - то оно имеет приоритет над дефолтным.
    # validate_default - будет ли валидироваться значение по умолчанию или допускается несостыковка типов, если истина то попытается произвести изменение типа данных в необходимое значение

    postcode: Literal [394068, 394000]
    # хардкодное закрепление того значения, что должно быть в данных, иначе ошибка валидации. Если ложь - поругается, но запихнёт значение в атрибут как есть
    hobby: str = Field(pattern=r'^[a-zA-Z0-9_]{3,6}$')
    # значение должно соответствовать паттерну, или ошибка валидации
    # r'здесь условие паттерна' - Префикс `r` указывает, что строка является "сырой" (raw string). Это значит, что обратные слэши (`\`) внутри строки не будут интерпретироваться как специальные символы, что удобно при работе с регулярными выражениями.
    # ^ - символ обозначает начало строки. Он указывает, что совпадение должно начинаться с самого начала строки.
    # [a-zA-Z0-9_] - Это класс символов, который определяет допустимые символы в строке `a-z`: все строчные буквы от 'a' до 'z', `A-Z`: все заглавные буквы от 'A' до 'Z',`0-9`: все цифры от '0' до '9', `_`: символ подчеркивания.
    # {3,6} - Эта часть указывает на количество повторений символов из предыдущего класса
    # $ - Этот символ обозначает конец строки. Он указывает, что совпадение должно заканчиваться в самом конце строки

    car: str = Field(coerce_numbers_to_str=True)
    #  при валидации и создании экземпляра модели все числовые значения (например, int или float) будут автоматически преобразованы в строки (str)

    temp: float = Field(multiple_of=0.1)
    # значение должно быть кратно значению multiple_of иначе исключение

    value: condecimal(max_digits=4, decimal_places=2)
    # max_digits - общее количество цифр (включая цифры до и после десятичной точки) decimal_places - количество цифр после десятичной точки

    middle_name: str = Field(min_length=5, max_length=14)
    # ограничение по количеству символов

    card_num: Union[int, float, str] = Field(union_mode='left_to_right')
    # Union - объединяет несколько типов данных, union_mode='smart' проверяет на соответствие одному из типов, не пытаясь изменить, union_mode='left_to_right' - будет пытаться преобразовать поочерёдно в один из типов данных наичная с лева на право

    settings: condict(str, int)


data = {'id': 2,
        'firstname': 'Sergey',
        'age': 37,
        'lastname': 'Laba',
        'birthday_date': '1987-12-04',
        'password': '!QAZ1qaz',
        'postcode': 394068,
        'hobby': 'airGUN',
        'car': 2110,
        'temp': 36.6,
        'value': 12.1,
        'middle_name': 'Aleksandrovich',
        'card_num': "123.054"
        }


user = User(**data)

print("Проверка как выводит функция repr-", repr(user))

user_dict = user.model_dump()
# user_dict = user.model_dump(exclude={'id'})           # пример исключения из сериализации
user_json = user.model_dump_json()


print(type(user_dict), '\n', user_dict)




"""
default: Any = PydanticUndefined,
*,
default_factory: () -> Any | (dict[str, Any]) -> Any | None = _Unset,
alias: str | None = _Unset,
alias_priority: int | None = _Unset,                                    # не удалось выяснить
validation_alias: str | AliasPath | AliasChoices | None = _Unset,
serialization_alias: str | None = _Unset,
title: str | None = _Unset,
field_title_generator: (str, FieldInfo) -> str | None = _Unset,
description: str | None = _Unset,
examples: list | None = _Unset,
exclude: bool | None = _Unset,
discriminator: str | Discriminator | None = _Unset,                     # не удалось выяснить
deprecated: deprecated | str | bool | None = _Unset,                    # не удалось выяснить
json_schema_extra: dict[str, int | float | str | bool | None | list] | (dict[str, int | float | str | bool | None | list]) -> None | None = _Unset,
frozen: bool | None = _Unset,
validate_default: bool | None = _Unset,
repr: bool = _Unset,
init: bool | None = _Unset,
init_var: bool | None = _Unset,
kw_only: bool | None = _Unset,
pattern: str | Pattern[str] | None = _Unset,
strict: bool | None = _Unset,
coerce_numbers_to_str: bool | None = _Unset,
gt: SupportsGt | None = _Unset,
ge: SupportsGe | None = _Unset,
lt: SupportsLt | None = _Unset,
le: SupportsLe | None = _Unset,
multiple_of: float | None = _Unset,
allow_inf_nan: bool | None = _Unset,
max_digits: int | None = _Unset,
decimal_places: int | None = _Unset,
min_length: int | None = _Unset,
max_length: int | None = _Unset,
union_mode: Literal['smart', 'left_to_right'] = _Unset,
fail_fast: bool | None = _Unset) -> Any
"""