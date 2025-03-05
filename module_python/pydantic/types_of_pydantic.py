from typing import Annotated

from pydantic import BaseModel, Field, condecimal, constr


class User(BaseModel):
    id: int = Field(frozen=True)


    name: constr(min_length=1, max_length=5)
