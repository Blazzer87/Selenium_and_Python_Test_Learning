

import psycopg2
import pytest

@pytest.fixture()
def db_connect():
    sso_cursor = None
    sso_connect = None
    try:
        sso_connect = psycopg2.connect(database="reestr_sso", user="postgres", password="1qaz!QAZ",
                                       host="192.168.100.13", port="5432")
        print("\nсоединение создано")
        sso_cursor = sso_connect.cursor()
        print(" курсор создан")
        yield sso_cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при работе с PostgreSQL:", error)
    finally:
        if sso_cursor is not None:
            sso_cursor.close()
            print("курсор закрыт")
        if sso_connect is not None:
            sso_connect.close()
            print("соединение закрыто")


def test_get_verification_code(db_connect):
    db_connect.execute(
        "SELECT verification_code FROM verification_requests ORDER BY verification_request_id DESC LIMIT 1;"
    )
    code = int(db_connect.fetchone()[0])
    print(code)

