import requests
import urllib3

# Подавляем предупреждение InsecureRequestWarning от urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.post(url='https://192.168.100.120/auth/realms/qPlaner/protocol/openid-connect/token',
                         data={"username" : "laba", "password" : "!QAZ1qaz"},
                         verify=False)

print(response.status_code)

print(response.text)