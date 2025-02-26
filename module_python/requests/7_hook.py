import requests



base_url= "https://rahulshettyacademy.com"
key = "qaclick123"
endpoint = "/maps/api/place/add/json"+"?key="+f"{key}"

url = base_url+endpoint

json = {"location": {"lat": -38.383494,"lng": 33.427362},"accuracy": 50,"name": "Frontline house","phone_number": "(+91) 983 893 3937","address": "29, side layout, cohen 09","types": ["shoe park","shop"],"website": "http://google.com","language": "French-IN"}

def hook_print_text(*args, **kwargs):
    print("давай проверим как работают хуки и выведем это сообщение после получения ответа"
          "\nесли хуков два - то они должны передаваться в виде списка по образцу ниже")

def hook_print_response(response, *args, **kwargs):
    print("а здесь подъехал второй хук -", response.json())

hooks = {'response': [hook_print_text, hook_print_response]}            # названия хука предустановлено в библиотеке и их нельзя называть произвольно, только response - Ответ, сформированный на основе запроса.

response = requests.post(url=url, json=json, headers=header1|header2, hooks=hooks)




