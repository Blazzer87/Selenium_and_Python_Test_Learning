import requests

base_url= "https://rahulshettyacademy.com"
key = "qaclick123"
endpoint = "/maps/api/place/add/json"+"?key="+f"{key}"

url = base_url+endpoint

response_hook = {}


response = requests.post(
    url="https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123",
    params= {'key1': 'value1', 'key2': 'value2'},
    #files={'file': ('filename.txt', open('filename.txt', 'rb'))},
    hooks={'response': response_hook},
    json={"location": {"lat": -38.383494,"lng": 33.427362},"accuracy": 50,"name": "Frontline house","phone_number": "(+91) 983 893 3937","address": "29, side layout, cohen 09","types": ["shoe park","shop"],"website": "http://google.com","language": "French-IN"},
    headers={'test1': 'Test2/json', 'test3-Type': 'test4/json'},
    data={"location": {"lat": -38.383494,"lng": 33.427362},"accuracy": 50,"name": "Frontline house","phone_number": "(+91) 983 893 3937","address": "29, side layout, cohen 09","types": ["shoe park","shop"],"website": "http://google.com","language": "French-IN"},
    cookies={'session_id': '123456789'},
    auth=('user', 'pass'),
    timeout=5,
    allow_redirects=True,
    stream=False,
    verify=True,
    #cert=('/path/to/cert.pem', '/path/to/key.pem'),
    #proxies={'http': 'http://10.10.1.10:3128', 'https': 'http://10.10.1.10:1080'}
    )

"""**url** (строка): URL-адрес, на который будет отправлен запрос. В вашем примере это `url`
params (dict или bytes): • Используется для передачи параметров в URL-запроса (в строку запроса). Это полезно, если вам нужно передать параметры, которые должны быть добавлены к URL.
files (dict):    • Используется для отправки файлов на сервер. Словарь должен содержать имя поля формы как ключ и кортеж из имени файла, объекта файла или байтового потока как значение.
hooks (dict):    • Позволяет вам передавать функции обратного вызова (callbacks), которые будут вызваны при определенных событиях, таких как завершение запроса или получение ответа.
**data** (dict, bytes, или file-like object): Данные, которые будут отправлены в теле запроса. отправляет данные в формате application/x-www-form-urlencoded.
**json** (dict): Если вы хотите отправить JSON-данные, вы можете использовать этот параметр. Библиотека автоматически сериализует данные в JSON и устанавливает заголовок `Content-Type` в `application/json`.
**headers** (dict): Заголовки, которые вы хотите отправить с запросом. В вашем примере вы используете `header1 | header2`, что предполагает использование объединения словарей (в Python 3.9+)
**cookies** (dict или CookieJar): Куки, которые будут отправлены с запросом
**auth** (tuple): Кортеж для базовой аутентификации (username, password)
**timeout** (float или tuple): Время ожидания ответа от сервера в секундах
**allow_redirects** (bool): Указывает, следует ли следовать за перенаправлениями. По умолчанию это `True`.
**stream** (bool): Указывает, следует ли не загружать тело ответа сразу. По умолчанию это `False`. Полезно для работы с большими файлами
**verify** (bool или str): Указывает, следует ли проверять SSL-сертификат. Можно указать путь к CA_BUNDLE файлу или `False`, чтобы отключить проверку
cert (str или tuple):    • Используется для указания SSL-сертификата, который будет использоваться для проверки сервера. Можно указать путь к файлу сертификата или кортеж с путями к файлам сертификата и ключа.
**proxies** (dict): Словарь прокси-серверов для использования при запросе
"""


print(response.request.url)
print(response.request.headers)
print(response.request.method)
print(response.request.body)
print(response.request.hooks)
print(response.request.path_url)

