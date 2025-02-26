import requests

requests.get('https://github.com/', timeout=0.001)      #

"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPSConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)"""


r = requests.get('https://github.com', timeout=(3.05, 27))

""" 
1. Первое значение (3.05): Это время в секундах, в течение которого будет ожидаться установка соединения с сервером. 
Если соединение не будет установлено в течение этого времени, будет вызвано исключение requests.exceptions.Timeout.
2. Второе значение (27): Это время в секундах, в течение которого будет ожидаться ответа от сервера после успешного установления соединения. 
Если сервер не ответит в течение этого времени, также будет вызвано исключение requests.exceptions.Timeout.
Таким образом, в вашем примере вы устанавливаете таймаут на 3.05 секунды для подключения и 27 секунд для ожидания ответа от сервера после подключения.
"""