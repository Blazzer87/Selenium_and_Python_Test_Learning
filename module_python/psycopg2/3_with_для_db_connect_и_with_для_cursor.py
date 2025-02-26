import psycopg2

host = "192.168.100.13"
database = "reestr_sso"
user = "postgres"
password = "1qaz!QAZ"
port = "5432"

with psycopg2.connect(database=database, host=host, user=user, password=password, port=port) as db_connect:             # Используем контекстный менеджер для соединения с БД

    with db_connect.cursor() as cursor:                     # Используем контекстный менеджер для курсора
        cursor.execute("SELECT * FROM roles")               # Выполняем SQL запрос
        rows = cursor.fetchall()                            # Получаем все записи
        print(rows)

