import pytest
import requests


@pytest.fixture
def test_find_last_pmi_record():
    import psycopg2
    from psycopg2.extras import RealDictCursor
    host = "192.168.100.17"
    database = "vdcs3"
    user = "postgres"
    password = "pt_RQoCq2m_SZ8m2"
    port = "54320"
    db_connect = None
    try:
        db_connect = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)
        with db_connect.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("select code from kind where code like 'pmi-%' order by code desc limit 1")
            row = cursor.fetchall()
            import re
            current_num = re.sub(r'[a-zA-Z_-]', '',(row[0]['code']))
            next_num = int(current_num) + 1
            return next_num
    except Exception as error:
        print("Ошибка", error)
    finally:
        if db_connect is not None:
            db_connect.close()  # Закрываем соединение
            print("Соединение закрыто")


@pytest.fixture
def access_token():
    response = requests.post(url='http://192.168.100.17:18080/auth/realms/qpd/protocol/openid-connect/token',
                             headers={'Content-Type': 'application/x-www-form-urlencoded'},
                             data={'client_id': 'vdcs3-dev',
                                   'grant_type': 'password',
                                   'client_secret': 'xHUokMjWsrMuBIXugXFdrqvzVEbgvr',
                                   'username': 'vdcs3tst',
                                   'password': 'Co_ZLHb5ao'}
                             )
    return response.json()['access_token']


def test_create_kind(access_token, test_find_last_pmi_record):
    response = requests.post(url='http://192.168.100.17:4000/api/context/v1/kind',
                             headers={'Content-Type': 'application/json'}|{'Authorization': f'Bearer {access_token}'},
                             json={'code': f'pmi-kind{test_find_last_pmi_record}', 'description':'anything'})
    print(response.request.body)
    print(response.status_code)
    print(response.json())


def test_create_vendor(access_token):
    response = requests.post(url='http://192.168.100.17:4000/api/context/v1/vendor',
                             headers={'Content-Type': 'application/json'}|{'Authorization': f'Bearer {access_token}'},
                             json={'code': 'testlaba', "subscribers": []}
                             )
    print(response.request.body)
    print(response.status_code)
    print(response.json())


def test_get_keycloack_token():
    response = requests.post(url='https://192.168.100.17:4000/auth/realms/{realm}/protocol/openid-connect/token',
                             headers={'Content-Type': 'application/x-www-form-urlencoded'},
                             verify=False,
                             data={'client_id': 'admin-cli',
                                   'grant_type': 'client_credentials',
                                   'client_secret': 'xHUokMjWsrMuBIXugXFdrqvzVEbgvr',
                                   # 'username': 'vdcs3tst',
                                   # 'password': 'Co_ZLHb5ao'
                                   }
                             )
    print(response.request.body)
    print(response.status_code)
    print(response.json())