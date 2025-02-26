from pydantic import BaseModel, ValidationError

class Tag(BaseModel):
    id: int
    tag: str

class City(BaseModel):
    city_id: int
    name: str
    tags: list[Tag]


input_json = """{
    "city_id": 123,
    "name": "Moscow",
    "tags": [{
        "id": 1,
        "tag": "capital"
    },{
        "id": 2,
        "tag": "big_city"
    }]
}"""


try:
    city = City.model_validate_json(input_json)

except ValidationError as e:
    print(f"нарушена валидация \n, {e.json()}")

else:
    print(city)
    print(city.tags[1].tag)
