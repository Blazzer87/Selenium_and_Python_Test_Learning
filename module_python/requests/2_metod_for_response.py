import requests
from requests.status_codes import codes
from requests import status_codes

from Module_Python.requests.headers_union_and_use import header1,header2

base_url= "https://rahulshettyacademy.com"
key = "qaclick123"
endpoint = "/maps/api/place/add/json"+"?key="+f"{key}"

url = base_url+endpoint


json = {
        "location": {
        "lat": -38.383494,
        "lng": 33.427362
        },
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
        "shoe park",
        "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
        }

response2 = requests.post(url=url, json=json, headers=header1|header2)

#print(response2)                        # <Response [200]>
#print(response2.headers)                # выведет все хедеры в ответа
#print(response2.status_code)            # 200
#print(response2.json())                 # выведет тело ответа в формате json {'status': 'OK', 'place_id': '30c6f3dfefe3109d580e395bbb789ac7', 'scope': 'APP', 'reference': '13a441c7f37cd87f3119076772417a5113a441c7f37cd87f3119076772417a51', 'id': '13a441c7f37cd87f3119076772417a51'}
#print(response2.text)                   # вывод в текстовом формате - {"status":"OK","place_id":"4e57f01b811498471b9b995f4d260573","scope":"APP","reference":"1155d6376de2359fca97be28b81a90771155d6376de2359fca97be28b81a9077","id":"1155d6376de2359fca97be28b81a9077"}
#print(response2.url)                    # https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123
#print(response2.history)                # Список объектов Response, представляющих промежуточные ответы (если были перенаправления).
#print(response2.cookies)                # Объект, представляющий куки, полученные от сервера.
"""Ответ <RequestsCookieJar[]> означает, что в результате выполнения вашего запроса не было получено ни одного cookie от сервера. 
Как проверить наличие cookies? 
сли вы хотите убедиться, что cookies действительно не были отправлены, вы можете просмотреть заголовки ответа:
print(response2.headers)
Если вы ожидаете, что сервер должен отправить cookies, убедитесь, что вы правильно настроили запрос и проверили документацию API или сервиса, к которому обращаетесь."""

#print(response2.raise_for_status())     # читай ниже
"""Метод raise_for_status() не генерирует исключение, только если HTTP-статус код указывает на успешный запрос. Это означает, что он не вызовет исключение для следующих кодов:
• 200 OK: Запрос выполнен успешно.
• 201 Created: Запрос выполнен успешно, и ресурс был создан.
• 202 Accepted: Запрос принят, но еще не обработан.
• 204 No Content: Запрос выполнен успешно, но нет содержимого для возврата.
• 205 Reset Content: Запрос выполнен успешно, и клиент должен сбросить представление документа.
• 206 Partial Content: Запрос выполнен успешно, и сервер возвращает часть ресурса.
Для всех других кодов состояния (например, 4xx и 5xx), метод raise_for_status() вызовет исключение HTTPError."""

# print(response2.encoding)               # Этот атрибут возвращает кодировку, используемую для декодирования ответа. Обычно она определяется на основе заголовка Content-Type. Вы можете изменить это значение, если хотите использовать другую кодировку.
# print(response2.elapsed)                # Этот атрибут возвращает объект timedelta, который показывает, сколько времени прошло с момента отправки запроса до получения ответа. Это может быть полезно для мониторинга производительности.
# print(response2.links)          #  Этот атрибут возвращает словарь, содержащий ссылки, указанные в заголовках Link, если они есть. Это может быть полезно для работы с API, которые используют пагинацию.

assert response2.status_code != requests.codes.ok







