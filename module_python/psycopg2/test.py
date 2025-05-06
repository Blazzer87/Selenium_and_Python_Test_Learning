import psycopg2

dbconnect = psycopg2.connect()

cursor = dbconnect.cursor()

cursor.execute(запрос)

cursor.fetchone()