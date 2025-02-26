from collections import ChainMap
import requests


header1 = {"Accept": "application/json"}
header2 = {"Content-Type": "application/json"}

base_url= "https://rahulshettyacademy.com"
key = "qaclick123"
endpoint = "/maps/api/place/add/json"+"?key="+f"{key}"
url = base_url+endpoint
json = {"location": {"lat": -38.383494,"lng": 33.427362},"accuracy": 50,"name": "Frontline house","phone_number": "(+91) 983 893 3937","address": "29, side layout, cohen 09","types": ["shoe park","shop"],"website": "http://google.com","language": "French-IN"}
response = requests.post(url=url, json=json, headers=header1|header2)



# объединение хедеров МЕТОД 1 - лучший метод через оператор |
print("metod 1", header1 | header2)


# объединение хедеров МЕТОД 2 - чистое объединение через распаковку внутрь нового словаря
all_header = {**header1, **header2}
# print("metod 2", all_header)


# объединение хедеров МЕТОД 3 - через перезапись 1ого словаря
header1.update(header2)
# print("metod 3", header1)


# объединение хедеров МЕТОД 4 - через стороннюю библиотеку collections
all_header2 = dict(ChainMap(header2, header1))
# print("metod 4", all_header2)

"""Согласно RFC 7230 , имена HTTP-заголовков нечувствительны к регистру."""


"""Обращение к хедерам через респонс"""
#print(response.headers['Content-Type'])              # 'application/json'
#print(response.headers.get('content-type'))        # 'application/json'


