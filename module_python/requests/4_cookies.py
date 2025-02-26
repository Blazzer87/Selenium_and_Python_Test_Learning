import requests

url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print(r.text)                       # '{"cookies": {"cookies_are": "working"}}'