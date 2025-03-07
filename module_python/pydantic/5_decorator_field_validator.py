from pydantic import BaseModel, field_validator, ValidationError

class User(BaseModel):
    email: str
    age: int

    @field_validator('email', mode='before')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email address')
        return value

    @field_validator('age')
    def validate_age(cls, value):
        if value < 0:
            raise ValueError('Age must be a positive integer')
        return value

# Пример создания объекта
try:
    user = User(email='test@example.com', age=25)
    print("Пользователь успешно создан:\n", user)
except ValidationError as e:
    print("Ошибка валидации:", e)
