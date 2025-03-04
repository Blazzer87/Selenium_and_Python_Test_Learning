import json

from pydantic import BaseModel, ValidationError
from pydantic.json_schema import model_json_schema


class Tag(BaseModel):
    id: int
    tag: str

class City(BaseModel):
    city_id: int
    name: str
    tags: list[Tag]

input_json = """{"city_id": 123,"name": "Moscow","tags": [{"id": 1,"tag": "capital"},{"id": 2,"tag": "big_city"}]}"""
input_dict = {"city_id": 123,"name": "Moscow","tags": [{"id": 1,"tag": "capital"},{"id": 2,"tag": "big_city"}]}

# """1. Метод model_dump() (устаревший dict()) применяется к объекту класса-модели, возвращает данные в формате СЛОВАРЯ"""
# try: city = City.model_validate_json(input_json)
# except ValidationError as e: print(f"нарушена валидация \n, {e.json()}")
# else:
#     print(city)                     # city_id=123 name='Moscow' tags=[Tag(id=1, tag='capital'), Tag(id=2, tag='big_city')]
#     print(city.model_dump())        # {'city_id': 123, 'name': 'Moscow', 'tags': [{'id': 1, 'tag': 'capital'}, {'id': 2, 'tag': 'big_city'}]}
#
# """2. Метод model_dump_json() (устаревший json()) применяется к объекту класса-модели, возвращает данные в формате ДЖЕЙСОН"""
# try: city = City.model_validate_json(input_json)
# except ValidationError as e: print(f"нарушена валидация \n, {e.json()}")
# else:
#     print(city)                         # city_id=123 name='Moscow' tags=[Tag(id=1, tag='capital'), Tag(id=2, tag='big_city')]
#     print(city.model_dump_json())        # {"city_id":123,"name":"Moscow","tags":[{"id":1,"tag":"capital"},{"id":2,"tag":"big_city"}]}
#
# """3. Метод model_copy() (устаревший copy()) применяется к объекту класса-модели, возвращает СТРОКОВОЕ значение """
# try: city = City.model_validate_json(input_json)
# except ValidationError as e: print(f"нарушена валидация \n, {e.json()}")
# else:
#     print(city)                     # city_id=123 name='Moscow' tags=[Tag(id=1, tag='capital'), Tag(id=2, tag='big_city')]
#     print(city.model_copy())        # city_id=123 name='Moscow' tags=[Tag(id=1, tag='capital'), Tag(id=2, tag='big_city')]

# """4. Метод model_validate() (устаревший parse_obj()) применяется к самой Модели, принимает только СЛОВАРЬ, возвращает СТРОКОВОЕ значение """
# city = City.model_validate(input_dict)
# print(type(city),city)
#
# """5. Метод model_validate_json() (устаревший parse_raw()) применяется к самой Модели, принимает только СТРОКУ, возвращает СТРОКОВОЕ значение """
# city = City.model_validate_json(input_json)
# print(city)

# """6. Метод model_json_schema() (устаревший schema() или schema_json()) принимает в себя Модель, возвращает СХЕМУ ВАЛИДАЦИИ модели, которую прогоняем через json.dumps для удобоваримости """
# model = City.model_json_schema()
# print(model)
# print((json.dumps(model, indent=2)))

# """7. Метод model_construct() (устаревший construct()) принимает РАСПАКОВАННЫЙ СЛОВАРЬ, создаёт объект класса НЕ ПРОВОДЯ валидацию данных, работает в в 30 раз быстрее, чем создание модели с полной проверкой, используется для уже проверенных данных"""
# model = City.model_construct(**input_dict)
# print(model)








