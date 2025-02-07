import psycopg2

host = "192.168.100.13"
database = "reestr_sso"
user = "postgres"
password = "1qaz!QAZ"
port = "5432"

db_connect = None                               # определяется переменная за пределами try/except чтобы не возникало ошибки

try:
    db_connect = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)      # создаётся объект класса psycopg2, к нему вызывается метод коннект, в параметры которого передаются параметры для подключения

    cursor = db_connect.cursor()                # создаём курсор

    cursor.execute("SELECT * FROM roles")       # передаём в курсор SQL запрос через метод execute()
    row = cursor.fetchall()                     # fetchall выводит все найденные записи
    print(row)
    cursor.execute("SELECT * FROM roles")       # передаём в курсор SQL запрос через метод execute()
    row = cursor.fetchone()                     # fetchone выводит только первую найденную запись
    print(row)
    cursor.execute("SELECT * FROM roles")       # передаём в курсор SQL запрос через метод execute()
    row = cursor.fetchmany(2)                   # fetchmany выводит кол-во записей переданное в параметрах, если параметры пусты - выводит 1ую строку
    print(row)

    print('\n')

    cursor.execute("SELECT verification_code FROM verification_requests ORDER BY verification_request_id DESC LIMIT 5")
    row = cursor.fetchall()                      # fetchall выводит все найденные записи
    print(row)
    cursor.execute("SELECT verification_code FROM verification_requests ORDER BY verification_request_id DESC LIMIT 5")
    row = cursor.fetchone()[0]                    # fetchone выводит только первую найденную запись
    print(row)
    cursor.execute("SELECT verification_code FROM verification_requests ORDER BY verification_request_id DESC LIMIT 5")
    row = cursor.fetchmany(2)                   # fetchmany выводит кол-во записей переданное в параметрах, если параметры пусты - выводит 1ую строку
    print(row)

    print('\n')

    print('Полученный набор данных возвращается в виде списка, внутрь которого помещён кортеж.''\n'
          'Обращение происходит по индексу к обоим из них''\n'
          'Например получим "Administrator" - 2-ой элемент из 2-ого кортежа в наборе данных возвращаемом из role''\n')

    cursor.execute("SELECT * FROM roles")
    row = cursor.fetchall()[1][1]
    print(row)

except Exception as error:
    print("Ошибка", error)

finally:
    if db_connect:
        db_connect.close()
        print("Соединение закрыто")
