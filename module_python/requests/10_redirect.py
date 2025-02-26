"""По умолчанию Requests будет выполнять перенаправление местоположения для всех глаголов, кроме HEAD.
Мы можем использовать historyсвойство объекта Response для отслеживания перенаправления.
Список Response.historyсодержит Responseобъекты, которые были созданы для выполнения запроса. Список отсортирован от самого старого до самого последнего ответа.
Например, GitHub перенаправляет все HTTP-запросы на HTTPS: пример смотри ниже"""
import requests

r = requests.get('http://github.com/')          # отправляем HTTP-запрос, не HTTPS !!!

print(r.url)                   # 'https://github.com/'

print(r.status_code)            # 200

print(r.history)                # [<Response [301]>]