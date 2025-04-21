import pytest
import requests



import requests

from test_my_experiments_and_expirience.vdcs.test_2 import access_token

url = "http://192.168.100.17:4000/api/participant/v1/search"

querystring = {"query":""}

headers={'Content-Type': 'application/json'}|{'Authorization': f'Bearer {access_token}'}

response = requests.get(url, params=querystring, headers=headers)

print(response)