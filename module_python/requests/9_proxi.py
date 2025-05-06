import requests



""" метод 1 на прямую"""

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

r = requests.get('http://example.org', proxies=proxies)
print(r.history)




""" метод 2 через сессию"""

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
session = requests.Session()
session.proxies.update(proxies)

session.get('http://example.org')