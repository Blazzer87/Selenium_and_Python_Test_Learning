from pydantic import BaseModel, field_validator, model_validator, ValidationError, validate_call


class User(BaseModel):
    email: str
    password: str
    confirm_password: str

    @validate_call
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email address')
        return value

    @model_validator('password')
    def check_passwords_match(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueError('Passwords do not match')
        return values

# Пример создания объекта
try:
    user = User(email='test@example.com', password='secret', confirm_password='secret')
    print("Пользователь успешно создан:\n", user)
except ValidationError as e:
    print("Ошибка валидации:", e)
