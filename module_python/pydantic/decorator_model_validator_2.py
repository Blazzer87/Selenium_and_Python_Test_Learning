from pydantic import BaseModel, field_validator, model_validator
from datetime import date

class User(BaseModel):
    id: int
    name: str
    birthday_date: date

    @field_validator('name', mode='before')
    def validate_name(cls, v):
        if isinstance(v, int):
            return str(v)
        elif isinstance(v, str):
            return v
        else:
            raise ValueError("Имя должно быть строкой или числом")

    @model_validator(mode='after')
    def check_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year - (
            (today.month, today.day) < (self.birthday_date.month, self.birthday_date.day))

        if age < 18:
            raise ValueError("Пользователь должен быть старше 18 лет")
        if age > 120:
            raise ValueError("Возраст не может превышать 120 лет")
        return self

    @model_validator(mode='after')
    def set_default_name(self):
        if self.name.strip() == '':
            self.name = f"User_{self.id}"
        return self


try:
    user = User(id=1, name="John", birthday_date=date(2000, 1, 1))
    print(user)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    user = User(id=2, name="", birthday_date=date(2010, 1, 1))
    print(user)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    user = User(id=3, name="Alice", birthday_date=date(1900, 1, 1))
    print(user)
except ValueError as e:
    print(f"Ошибка: {e}")

