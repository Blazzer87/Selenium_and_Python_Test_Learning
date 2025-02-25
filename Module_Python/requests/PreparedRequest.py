from requests import Request, Session
import requests

session = requests.Session()
url, json, headers  = 'https://httpbin.org',"{'name':'sergey'}",{'x-test': 'true'}  # строка + строка + словарь


req = Request('POST', url, json=json, headers=headers)      # создали реквест без отправки

print(req.json)         # {'name':'sergey'}
print(req.url)         # https://httpbin.org
print(req.headers)         # {'x-test': 'true'}
# убедились что запрос полностью собран как нам надо

prepped = req.prepare()      # Метод prepare() создает "подготовленный" запрос (объект PreparedRequest), который включает в себя все данные, необходимые для отправки HTTP-запроса.
# Это включает в себя URL, заголовки, данные и параметры.

prepped2 = session.prepare_request(req)


print("тело запроса - ",prepped.body)

prepped.body = 'я решил изменить тело.'

print("новое тело запроса - ",prepped.body)

settings = session.merge_environment_settings(prepped.url, {}, None, None, None)    # # можно влить определённые настройки сессию - url proxy stream verify cert

resp = session.send(prepped, **settings)      # отправляю подготовленный запрос? добавляю к нему дополнительные настройки по желанию

print(resp.text)                # ответ будет ошибочный так как запрос собран от балды