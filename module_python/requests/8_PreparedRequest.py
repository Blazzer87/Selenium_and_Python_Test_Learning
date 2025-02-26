from requests import Request, Session
import requests

session = requests.Session()
url, json, headers  = 'https://httpbin.org',"{'name':'sergey'}",{'x-test': 'true'}  # строка + строка + словарь


req = Request('POST', url, json=json, headers=headers)      # создали реквест без отправки

print("test 1", req.json)         # {'name':'sergey'}
print("test 2",req.url)         # https://httpbin.org
print("test 3 текущие хедеры ",req.headers)         # {'x-test': 'true'}

req.headers = {'x-test222': 'true22222'}
print("test 4 я решил поменять хедеры",req.headers)         # {'x-test222': 'true22222'}

# убедились что запрос полностью собран как нам надо

prepped = req.prepare()      # Метод prepare() создает "подготовленный" запрос (объект PreparedRequest), который включает в себя все данные, необходимые для отправки HTTP-запроса.
# Это включает в себя URL, заголовки, данные и параметры.

prepped2 = session.prepare_request(req)


print("\ntest 5","тело запроса - ",prepped.body)

prepped.body = 'я решил изменить тело.'

print("test 6","новое тело запроса - ",prepped.body)

settings = session.merge_environment_settings(prepped.url, {}, None, None, None)    # # можно влить определённые настройки сессию - url proxy stream verify cert

resp = session.send(prepped, **settings)      # отправляю подготовленный запрос? добавляю к нему дополнительные настройки по желанию

print("test 7",resp.text)                # ответ будет ошибочный так как запрос собран от балды




