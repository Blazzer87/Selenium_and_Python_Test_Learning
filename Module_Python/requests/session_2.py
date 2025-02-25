import requests

session = requests.Session()            # создали сессию

session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')      # отправили запрос
response = session.get('https://httpbin.org/cookies')                       # отправили запрос и получили ответ

print(response.json())                       # вычитываем ответ '{"cookies": {"sessioncookie": "123456789"}}'


session.auth = ('user', 'pass')                 # передали в сессию пользовательские данные
session.headers.update({'x-test': 'true'})          # передали в сессию хедеры


session.get('https://httpbin.org/headers', headers={'x-test2': 'true'})         # мы отправили двойные хедеры, x-test2 в самом запросе, и x-test указав их ранее в запросе  'x-test' and 'x-test2' are sent


"""Обратите внимание, однако, что параметры уровня метода не будут сохраняться между запросами, даже если используется сеанс. 
Этот пример отправит файлы cookie только с первым запросом, но не со вторым:"""

session = requests.Session()                                                              # мы пересоздали сессию
response = session.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})        # куки переданы в теле запроса, но не присвоены к сессии, так как мы пересоздали сессию
print("куки есть в ответе, так как мы передали их аргументах запроса",response.text)                                      # куки есть в ответе '{"cookies": {"from-my": "browser"}}'


response = session.get('https://httpbin.org/cookies')
print("а здесь их нет так как в аргументах запроса их нет и к сессии не присвоены", response.text)                                      # '{"cookies": {}}'

session.cookies.update({'from-my2222': 'browser222222'})
response = session.get('https://httpbin.org/cookies')
print("но если куки передать в сессию, и не предавать в аргументах запроса то они будут", response.text)


"""Сессии также можно использовать в качестве менеджеров контекста:"""
with requests.Session() as s:
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
"""Это гарантирует, что сеанс будет закрыт сразу после withвыхода из блока, даже если возникнут необработанные исключения."""


"""Иногда вам нужно будет исключить ключи уровня сеанса из параметра dict. 
Чтобы сделать это, просто установите значение этого ключа в Noneпараметре уровня метода. Он будет автоматически исключен."""

