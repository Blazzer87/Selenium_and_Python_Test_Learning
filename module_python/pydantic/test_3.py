from pydantic import BaseModel, ValidationError, Field, validator, field_validator


class City(BaseModel):
    city_id: int
    name: str = Field (alias ='cityFullName')           # определяет чужой приходящий нейминг от стороннего ресурса

    @field_validator('name')
    def name_should_be_spb(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError("work with spb")
        return v


input_json = """{
    "city_id": 123,
    "cityFullName": "Moscow"
}"""


try:
    city = City.model_validate_json(input_json)

except ValidationError as e:
    print(f"нарушена валидация \n, {e.json()}")

else:
    print(city.model_dump_json())                       # перевод в json


