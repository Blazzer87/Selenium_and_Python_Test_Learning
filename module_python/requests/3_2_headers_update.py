import requests

# Создаем объект запроса с уже указанными заголовками
headers = {
    'User-Agent': 'OOOOOOLDmy-app/0.0.1',
    'Accept': 'OOOOOOLDapplication/json'
}
response = requests.get('https://example.com', headers=headers)

# Добавляем новые заголовки
new_headers = {
    'Authorization': 'TTTTTTESTBearer my-token',
    'Custom-Header': 'TTTTTTESTvalue'
}

# Обновляем заголовки
response.request.headers.update(new_headers)

# Проверяем заголовки
print(response.request.headers)