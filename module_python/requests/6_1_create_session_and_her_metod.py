import requests


header1 = {"Accept": "application/json"}
header2 = {"Content-Type": "application/json"}

base_url= "https://rahulshettyacademy.com"
key = "qaclick123"
endpoint = "/maps/api/place/add/json"+"?key="+f"{key}"

url = base_url+endpoint

json = {"location": {"lat": -38.383494,"lng": 33.427362},"accuracy": 50,"name": "Frontline house","phone_number": "(+91) 983 893 3937","address": "29, side layout, cohen 09","types": ["shoe park","shop"],"website": "http://google.com","language": "French-IN"}

session = requests.session()

session.close()       # Закрывает сессию и освобождает все ресурсы.
session.auth = ('username', 'password')           # Устанавливает аутентификацию для всех запросов в этой сессии.
print(session.headers)
session.headers.update({'AuthoriTTTTESzation': 'Bearer tEEEESoken'})         # Добавляет заголовки, которые будут отправляться с каждым запросом.
print(session.headers)
session.cookies.set('cookie_name', 'cookie_value')      # Получает или устанавливает куки для сессии.
session.cookies.get('cookie_name', 'cookie_value')      # Получает или устанавливает куки для сессии.
session.proxies = {'http': 'http://proxy.example.com:8080', 'https': 'http://proxy.example.com:8080'}       # Устанавливает прокси-серверы для сессии.
session.proxies = {'http': 'http://proxy.example.com:8080', 'https': 'http://proxy.example.com:8080'}       # Устанавливает проверку SSL-сертификатов (можно установить в False, если нужно игнорировать проверку).
response = session.get('https://example.com/largefile', stream=True)            # Устанавливает режим потока для загрузки больших файлов.
# session.prepare_request(prepped)            #
session.merge_environment_settings(url, {}, None, None, None)        # можно влить определённые настройки сессию - url proxy stream verify cert










