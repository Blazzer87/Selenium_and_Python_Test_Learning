
from typing import Annotated, Literal, Union, List, Optional, Any, Tuple, Set, Dict, Final
from pydantic import BaseModel, Field, condecimal, conint, constr, conlist


class User(BaseModel):
    id: Annotated [int, Field()]
    name: str
    age: int
    tag: Optional[str] = None


data = {'id': 2,
        'name': 'Sergey',
        'age': 30
        }

user = User(**data)

user_dict = user.model_dump()
user_json = user.model_dump_json()

print(type(user_dict), '\n', user_dict)