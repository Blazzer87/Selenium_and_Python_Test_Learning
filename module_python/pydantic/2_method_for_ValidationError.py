from pydantic import BaseModel, ValidationError

class Tag(BaseModel):
    id: bool
    tag: str

class City(BaseModel):
    city_id: str                    # заведомо ошибка
    name: str
    tags: list[Tag]

input_json = """{"city_id": 123,"name": "Moscow","tags": [{"id": 1,"tag": "capital"},{"id": 2,"tag": "big_city"}]}"""
input_dict = {"city_id": 123,"name": "Moscow","tags": [{"id": 1,"tag": "capital"},{"id": 2,"tag": "big_city"}]}

try:
    city = City.model_validate_json(input_json)

except ValidationError as e:
    print(f"\n e.errors() метод вернет список ошибок, найденных во входных данных. \n, {e.errors()}")
    print(f"\n e.json() метод вернет JSON-представление errors. \n, {e.json()}")
    print(f"\n str(e) метод вернет понятное для человека представление ошибок.. \n, {str(e)}")

"""
АТРИБУТЫ ОШИБОК:
loc - местоположение ошибки в виде списка. Первым элементом в списке будет поле, в котором произошла ошибка,а если поле является подмоделью , последующие элементы будут присутствовать для указания вложенного местоположения ошибки.
type - компьютерно-считываемый идентификатор типа ошибки.
msg - понятное человеку объяснение ошибки.
ctx - необязательный объект, содержащий значения, необходимые для отображения сообщения об ошибке.
"""
