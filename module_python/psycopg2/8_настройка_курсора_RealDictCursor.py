import psycopg2
from psycopg2.extras import RealDictCursor

host = "192.168.100.17"
database = "vdcs3"
user = "postgres"
password = "pt_RQoCq2m_SZ8m2"
port = "54320"

db_connect = None                                       # Определяем переменную db_connect

try:
    db_connect = psycopg2.connect(database=database, host=host, user=user, password=password, port=port)

    # with db_connect.cursor() as cursor:                 # создаём курсор
    #     cursor.execute("SELECT * FROM kind ORDER BY id DESC LIMIT 5 ")           # передаём в курсор SQL запрос через метод execute()
    #     row = cursor.fetchall()                         # fetchall выводит все найденные записи
    #     print(row)                                      # [(254, 'testlaba', 'anything'), (249, 'we', 'qwe'), (238, 'geqag', 'kdkir'), (236, 'qyqbv', 'rubjo'), (231, 'behco', 'pwkgx')]


        # аргумент RealDictCursor задаёт настройку для курсора чтобы он возвращал не кортежи, а словари, что позволяет обратиться по ключу

    with db_connect.cursor(cursor_factory=RealDictCursor) as cursor:                 # создаём курсор
        cursor.execute("SELECT * FROM kind ORDER BY id DESC LIMIT 5 ")           # передаём в курсор SQL запрос через метод execute()
        row = cursor.fetchall()                         # fetchall выводит все найденные записи
        print(row)                                      # [RealDictRow({'id': 254, 'code': 'testlaba', 'description': 'anything'}), RealDictRow({'id': 249, 'code': 'we', 'description': 'qwe'}), RealDictRow({'id': 238, 'code': 'geqag', 'description': 'kdkir'}), RealDictRow({'id': 236, 'code': 'qyqbv', 'description': 'rubjo'}), RealDictRow({'id': 231, 'code': 'behco', 'description': 'pwkgx'})]

        if row:  # Проверяем, что список не пустой
            first_id = row[1]['id']  # Обращаемся ко второму элементу и получаем значение id
            print("Первый id:", first_id)
        else:
            print("Нет записей.")


except Exception as error:
    print("Ошибка", error)

finally:
    if db_connect is not None:
        db_connect.close()                              # Закрываем соединение
        print("Соединение закрыто")