from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    username: str = Field(description="Имя пользователя")
    email: str = Field(description="Email адрес")
    age: int = Field(gt=0, description="Возраст пользователя")


    # Конфигурация модели
    model_config = ConfigDict(
        title='User Model',
        str_to_lower=True,
        validate_default=True,  # Включение валидации всех полей
        str_strip_whitespace=True,  # Удаление пробелов в начале и конце для строк
        extra='ignore'
    )

# Пример создания экземпляра модели
print("\n ВАЛИДНЫЙ ТЕСТ \n")
try:
    user = User(username='JOHN_doe ', email='john.DOE@EXAMPLE.com', age=30, id=123456789)
    print(user.model_dump_json())  # Вывод JSON с преобразованием строк в верхний регистр
except ValueError as e:
    print(e)

# # Попробуем создать пользователя с некорректным email
# print("\n неВАЛИДНЫЙ ТЕСТ \n")
# try:
#     invalid_user = User(username='invalid_user', email='invalid_email', age=-5)
# except ValueError as e:
#     print(e)  # Вывод ошибки валидации
