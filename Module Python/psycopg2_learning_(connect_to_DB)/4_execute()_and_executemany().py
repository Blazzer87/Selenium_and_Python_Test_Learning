import psycopg2

host = "192.168.100.13"
database = "reestr_sso"
user = "postgres"
password = "1qaz!QAZ"
port = "5432"

with psycopg2.connect(database=database, host=host, user=user, password=password, port=port) as db_connect:             # Используем контекстный менеджер для соединения с БД

    def create_ONE():
        with db_connect.cursor() as cursor:
            cursor.execute("INSERT INTO roles (role_id, code, name) VALUES (5,5,5), (6,6,6), (7,7,7), (8,8,8), (9,9,9)")               # Выполняем SQL запрос
            cursor.execute("SELECT * FROM roles")
            rows = cursor.fetchall()                            # Получаем все записи
            print(rows)


    def create_MANY():
        with db_connect.cursor() as cursor:
            SQLquery = "INSERT INTO roles (role_id, code, name) VALUES (%s,%s,%s)"
            # Обратите внимание на часть VALUES() в SQL-запросе, там можно увидеть знаки подстановки %s.
            # Они отвечают за значения, которые будут считаны из кортежа, а затем добавлены в базу данных.
            # Когда происходит чтение кортежа, то каждому элементу кортежа присваивается индекс по которому можно получить значение элемента.
            # И знаки подстановки %s, как раз отвечают за указание индекса элемента.
            # Чтобы метод executemany() успешно отработал, необходимо чтобы количество знаков подстановки %s и количество элементов в кортеже совпадало.
            data_table = [(10,10,10), (11,11,11), (12,12,12), (13,13,13), (14,14,14)]
            # передаём на вход список с несколькими кортежами
            cursor.executemany(SQLquery, data_table)
            cursor.execute("SELECT * FROM roles")               # Читаем что получилось
            rows = cursor.fetchall()                            # Получаем все записи
            print(rows)

create_MANY()

# но любая из указанных функций ничего не меняет в БД потому что нет обработки транзакции