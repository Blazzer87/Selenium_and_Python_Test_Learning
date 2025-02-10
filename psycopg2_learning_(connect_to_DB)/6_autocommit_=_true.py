import psycopg2

host = "192.168.100.13"
database = "reestr_sso"
user = "postgres"
password = "1qaz!QAZ"
port = "5432"

db_connect = None                                       # Определяем переменную db_connect

try:
    db_connect = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)

    db_connect.autocommit = True        # присваиваемое свойство автокоммит автосохраняет изменения без запроса коммита

    def create_ONE():
        with db_connect.cursor() as cursor:
            cursor.execute(
                "INSERT INTO roles (role_id, code, name) VALUES (99,99,99), (88,88,88), (77,77,77), (66,66,66), (55,55,55)")  # Выполняем SQL запрос
            cursor.execute("SELECT * FROM roles")
            rows = cursor.fetchall()  # Получаем все записи
            print(rows)

    create_ONE()

except Exception as error:

    db_connect.rollback()   # роллбэк отменяет транзакцию если что-то пошло не так.

    print("Ошибка", error)

finally:
    if db_connect is not None:
        db_connect.close()                              # Закрываем соединение
        print("Соединение закрыто")


