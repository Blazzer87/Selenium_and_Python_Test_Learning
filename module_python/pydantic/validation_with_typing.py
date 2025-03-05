
from typing import Annotated, Literal, Union, List, Optional, Any, Tuple, Set, Dict, Final
from pydantic import BaseModel, Field, condecimal, conint, constr, conlist


class Gun(BaseModel):
    air: Annotated[str, Field(default='pcp')]

x = [Gun()]

class User(BaseModel):
    id: Annotated [int, Field(frozen=True)]
    name: str
    age: Union [int | None]                         # Union объединяет два и более типов данных. None предполагает передачу age со значением None. Удаление age приведёт к ошибке
    money: Union [conint(ge=100) | None]            # Union может принимать условие
    items: Union[List[Gun], dict]                   # Union может объединять более сложные вариации типов с подвложениями
    # Использование Optional в Pydantic позволяет вам явно указывать, что поле может быть отсутствующим (т.е. иметь значение None).
    car: Optional[str]                              # Машина может быть строкой или None
    quantity: Optional [conint(gt=0)]               # Количество может быть положительным целым числом или None
    metadata: Any                                   # Поле может содержать данные любого типа
    hobbies: List [str]                             # Список строк
    position: Tuple [float, float, float]           # Кортеж из трех значений
    tags: Set [str]                                 # Множество строк
    preferences: Dict [str, str]                    # Словарь с ключами и значениями типа str
    version: Final [str] = "1.0.0"                  # для определения неизменяемых значений, это значение изменить нельзя
    count: conint(ge=0, le=100)                     # количество должно быть от 0 до 100
    username: constr (min_length=3, max_length=20)  # имя пользователя от 3 до 20 символов
    item: conlist (int, min_length=1, max_length=10)        # список с минимум 1 и максимум 10 целых чисел
    role: Literal['admin', 'user', 'guest']         # Поле может принимать только эти три значения


data = {'id': 2,
        'name': 'Sergey',
        'age': None,
        'money': 100,
        'items': x,
        'car': 'audi a8',
        'quantity': None,
        'metadata': x,
        'hobbies': ["reading", "hiking"],
        'position': (1.0, 2.0, 3.0),
        'tags': {"developer", "python", "openai"},
        'preferences': {"theme": "dark", "language": "en"},
        'version': 'НЕ ВАЖНО ЧТО ТУ БУДЕТ НАПИСАНО - FINAL не даст изменить',
        'count': 100,
        'username': 'alice',
        'item': [1, 2, 3],
        'role': 'admin'
        }


user = User(**data)
print(user.version)

user_dict = user.model_dump()
user_json = user.model_dump_json()

print(type(user_dict), '\n', user_dict)

