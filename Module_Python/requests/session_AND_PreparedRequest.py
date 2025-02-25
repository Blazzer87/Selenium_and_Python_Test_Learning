from requests import Request, Session
import requests

session = requests.Session()
url, json, cookies  = 'https://httpbin.org/cookies',"{'name':'sergey'}",{'cookie-testcookie': 'true'}  # строка + строка + словарь


req = Request('GET', url, json=json, cookies=cookies)      # создали реквест без отправки

print(req.json)         # {'name':'sergey'}
print(req.url)         # https://httpbin.org
print(req.cookies)         # {'x-test': 'true'}
# убедились что запрос полностью собран как нам надо

prepped = session.prepare_request(req)

print(prepped.body)         # b'"{\'name\':\'sergey\'}"'
print(prepped.url)         # https://httpbin.org/
# print(prepped.cookies)         # {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'x-test': 'true', 'Content-Length': '19', 'Content-Type': 'application/json'}
print(prepped.method)         # POST


session.cookies.update({'x-cookie': '213'})

resp = session.send(prepped)
print(resp.text)

resp2 = session.get("https://httpbin.org/cookies")
print(resp2.text)

"""данный запрос показывает что когда куки помещаются внутрь подготовленного запроса prepped,
а потом он отправляется через session.send то уходят только принадлежащие самому подготовленному запросу
и куки сессии в данном случае не отправляются
если хочешь отправить куки сессии то ты должен  запускать session.get() тогда улетают куки принадлежащие сессии"""