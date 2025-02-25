import requests

requests.get('https://github.com/', timeout=0.001)      #

"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPSConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)"""