from gevent.subprocess import value
from pydantic import BaseModel, Field, condecimal, field_validator, model_validator


class User(BaseModel):

    name: str = Field (default="test")
    age: int

    @field_validator('age')
    def age_validator(cls, value):
        if value > 18:
            raise ValueError("ошибка возраста")
        return value

    @model_validator(mode='before')
    def test_all(cls, value):
        if value['name'] != "Petr":
            raise ValueError("имя не петр")
        return value




Petr = User(age=17)

print(Petr)


