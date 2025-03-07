from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    username: str = Field(description="Имя пользователя")
    email: str = Field(pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$', description="Email адрес")
    age: int = Field(gt=0, description="Возраст пользователя")

    # Конфигурация модели
    model_config = ConfigDict(
        title='User Model',
        json_encoders={
            # Пример пользовательского кодировщика для типа данных
            str: lambda v: v.upper()  # Преобразование всех строк в верхний регистр при сериализации
        },
        validate_default=True,  # Включение валидации всех полей
        str_strip_whitespace=True,  # Удаление пробелов в начале и конце для строк
    )

# Пример создания экземпляра модели
print("\n ВАЛИДНЫЙ ТЕСТ \n")
try:
    user = User(username='john_doe ', email='john.doe@example.com', age=30)
    print(user.model_dump_json())  # Вывод JSON с преобразованием строк в верхний регистр
except ValueError as e:
    print(e)

# Попробуем создать пользователя с некорректным email
print("\n неВАЛИДНЫЙ ТЕСТ \n")
try:
    invalid_user = User(username='invalid_user', email='invalid_email', age=-5)
except ValueError as e:
    print(e)  # Вывод ошибки валидации
