import psycopg2

host = "192.168.100.13"
database = "reestr_sso"
user = "postgres"
password = "1qaz!QAZ"
port = "5432"

db_connect = None                                       # Определяем переменную db_connect

try:
    db_connect = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)

    with db_connect.cursor() as cursor:                 # создаём курсор
        cursor.execute("SELECT * FROM roles")           # передаём в курсор SQL запрос через метод execute()
        row = cursor.fetchall()                         # fetchall выводит все найденные записи
        print(row)

except Exception as error:
    print("Ошибка", error)

finally:
    if db_connect is not None:
        db_connect.close()                              # Закрываем соединение
        print("Соединение закрыто")