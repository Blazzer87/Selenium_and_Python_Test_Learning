import psycopg2
from psycopg2 import extensions         # новый импорт

host = "192.168.100.13"
database = "reestr_sso"
user = "postgres"
password = "1qaz!QAZ"
port = "5432"

db_connect = None                                       # Определяем переменную db_connect

try:
    db_connect = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)

    db_connect.autocommit = True        # присваиваемое свойство автокоммит автосохраняет изменения без запроса коммита


    """
    Констант psycopg2	Значение констант psycopg2	Название уровня изоляции PostgreSQL
    ISOLATION_LEVEL_READ_COMMITTED	1	READ COMMITTED
    ISOLATION_LEVEL_REPEATABLE_READ	2	REPEATABLE READ
    ISOLATION_LEVEL_SERIALIZABLE	3	SERIALIZABLE
    ISOLATION_LEVEL_READ_UNCOMMITTED	4	READ UNCOMMITTED
    """

    # Вывод текущего уровня изоляции транзакций
    print(f"Текущий уровень изоляции: {db_connect.isolation_level}")

    # Установка нового уровня изоляции транзакций
    db_connect.set_isolation_level(extensions.ISOLATION_LEVEL_SERIALIZABLE)
    print(f"Новый уровень изоляции: {db_connect.isolation_level}")


except Exception as error:
    db_connect.rollback()
    print("Ошибка", error)

finally:
    if db_connect is not None:
        db_connect.close()
        print("Соединение закрыто")