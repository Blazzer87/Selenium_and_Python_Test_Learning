from pydantic import BaseModel, validate_call, ValidationError

class User(BaseModel):
    username: str
    age: int

class UserService:

    @validate_call
    def create_user(self, username: str, age: int) -> User:
        return User(username=username, age=age)

# Пример использования
service = UserService()

try:
    user = service.create_user(username='JohnDoe', age=25)
    print("Пользователь успешно создан:", user)
except ValidationError as e:
    print("Ошибка валидации:", e)

# Ошибка валидации
try:
    user = service.create_user(username='Jo', age='twenty-five')  # Неверный тип для age
except ValidationError as e:
    print("Ошибка валидации:", e)
