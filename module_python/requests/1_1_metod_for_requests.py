import requests

from Module_Python.requests.headers_union_and_use import header1,header2

base_url= "https://rahulshettyacademy.com"
key = "qaclick123"
endpoint = "/maps/api/place/add/json"+"?key="+f"{key}"

url = base_url+endpoint


json = {"location": {"lat": -38.383494,"lng": 33.427362},"accuracy": 50,"name": "Frontline house","phone_number": "(+91) 983 893 3937","address": "29, side layout, cohen 09","types": ["shoe park","shop"],"website": "http://google.com","language": "French-IN"}

response = requests.post(url=url, json=json, headers=header1|header2)

requests.get()
requests.post()
requests.put()
requests.delete()
requests.head()
requests.options()
requests.patch()
requests.session()
"""создает объект сессии, который позволяет сохранять параметры и состояние между запросами. 
Это удобно для выполнения нескольких запросов к одному и тому же серверу, так как вы можете сохранить такие вещи, как куки, заголовки и другие параметры.
разбирается в отдельном файле"""
requests.request()
"""иной формат отправки запроса, когда метод указывается в аргументах
response = requests.request('GET', 'https://api.example.com/data')"""
requests.PreparedRequest()
"""представляет собой подготовленный HTTP-запрос. 
Это позволяет вам создать запрос с установленными параметрами (метод, URL, заголовки и т.д.) и отправить его позже. 
Это может быть полезно для повторного использования одного и того же запроса или для отладки."""
requests.exceptions.RequestException()
assert requests.codes.ok == response.status_code
