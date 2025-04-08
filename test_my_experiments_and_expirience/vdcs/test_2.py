import requests


def test_create_kind():
    response = requests.post(url="http://192.168.100.17:4000/api/context/v1/kind",
                             headers={"Content-Type": "application/json"},
                             json={"code": "test_laba"})
    print(response.status_code)
    print(response.json())