from datetime import date
from random import random

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    birthday_date: date

oleg = User(id=1,
            name='Oleg',
            birthday_date=date(year=1993, month=2, day=19))



oleg_dict = oleg.model_dump()
oleg_json = oleg.model_dump_json()
oleg_copy = oleg.model_copy()

print(type(oleg_dict),oleg_dict)
print(type(oleg_json),oleg_json)
print(type(oleg_copy),oleg_copy)



data = """{"id": 2, "name": "Max", "birthday_date": "2023-10-15"}"""

max = User.model_validate_json(data)
max_dict = max.model_dump()
max_json = max.model_dump_json()

print(type(max),max)
print(type(max_dict),max_dict)
print(type(max_json),max_json)


