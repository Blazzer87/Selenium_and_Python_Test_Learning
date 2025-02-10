import psycopg2

host = "192.168.100.13"
database = "reestr_sso"
user = "postgres"
password = "1qaz!QAZ"
port = "5432"

db_connect = None                                       # Определяем переменную db_connect

try:
    db_connect = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)

    def create_ONE():
        with db_connect.cursor() as cursor:
            cursor.execute(
                "INSERT INTO roles (role_id, code, name) VALUES (5,5,5), (6,6,6), (7,7,7), (8,8,8), (9,9,9)")  # Выполняем SQL запрос
            cursor.execute("SELECT * FROM roles")
            rows = cursor.fetchall()  # Получаем все записи
            print(rows)

    create_ONE()

    db_connect.commit()     # коммит закрывает транзакцию сохраняя её.

except Exception as error:

    db_connect.rollback()   # роллбэк отменяет транзакцию если что-то пошло не так.

    print("Ошибка", error)

finally:
    if db_connect is not None:
        db_connect.close()                              # Закрываем соединение
        print("Соединение закрыто")


