from pydantic import BaseModel, ValidationError, Field



class City(BaseModel):
    city_id: int
    name: str = Field (alias ='cityFullName')           # определяет чужой приходящий нейминг от стороннего ресурса


input_json = """{
    "city_id": 123,
    "cityFullName": "Moscow"
}"""


try:
    city = City.model_validate_json(input_json)

except ValidationError as e:
    print(f"нарушена валидация \n, {e.json()}")

else:
    print(city)
    print(city.model_dump_json())                       # перевод в json
    print(city.model_dump_json(by_alias=True))          # перевод в json с чужим неймингом
    print(city.model_dump_json(by_alias=True, exclude={'city_id'}))          # исключает вывод ключа и значения айди города

