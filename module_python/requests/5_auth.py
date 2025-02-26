import requests
from requests.auth import AuthBase


class PizzaAuth(AuthBase):
    """1. Создание объекта: Вы создаёте объект класса PizzaAuth с помощью PizzaAuth('kenneth'). Это просто создание экземпляра класса, и на этом этапе метод __call__ не вызывается."""
    def __init__ (self, username):
        self.username = username


    """3. Вызов метода __call__: Внутри библиотеки requests, когда она обрабатывает запрос, она вызывает метод __call__ вашего объекта PizzaAuth, передавая ему объект запроса. 
    Это позволяет вашему классу модифицировать запрос (например, добавлять заголовки) перед его отправкой."""
    def __call__(self, r):
        r.headers['X-Pizza'] = self.username
        return r

"""2. Передача в запрос: При вызове requests.get(...), библиотека requests видит, что вы передали объект PizzaAuth в параметр auth."""
requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))


"""Таким образом, хотя вы не вызываете метод __call__ напрямую, библиотека requests делает это за вас в процессе обработки запроса. 
Это и есть причина, по которой метод вызывается автоматически в вашем случае."""