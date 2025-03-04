
from datetime import date
from typing import Annotated

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str = Field(alias='firstname')        # управляет входящим неймингом полей из чужих данных
    age: int = Field(strict=True)       # если истина то включает строгий режим типизации, теперь "37" не переведётся в int самостоятельно
    lastname: str
    birthday_date: date = Field(title="этот тайтл не влияет на валидацию, а используется только для читаемости кода")

data = {'id': 2,
        'firstname': 'Sergey',
        'age': 37,
        'lastname': 'Laba',
        'birthday_date': '1987-12-04'}


user = User.model_validate(data)

user_dict = user.model_dump()
user_json = user.model_dump_json()


print(type(user_dict), '\n', user_dict)



"""
default: Any = PydanticUndefined,
*,
default_factory: () -> Any | (dict[str, Any]) -> Any | None = _Unset,
alias: str | None = _Unset,
alias_priority: int | None = _Unset,
validation_alias: str | AliasPath | AliasChoices | None = _Unset,
serialization_alias: str | None = _Unset,
title: str | None = _Unset,
field_title_generator: (str, FieldInfo) -> str | None = _Unset,
description: str | None = _Unset,
examples: list | None = _Unset,
exclude: bool | None = _Unset,
discriminator: str | Discriminator | None = _Unset,
deprecated: deprecated | str | bool | None = _Unset,
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