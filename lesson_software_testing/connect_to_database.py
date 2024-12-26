import psycopg2


def __init__(self):
    self.connection = None
    self.database = "reestr_sso"
    self.user = "postgres"
    self.password = "1qaz!QAZ"
    self.host = "192.168.100.13"
    self.port = "5432"


def connect(self):
    try:
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            port=self.port,
            user=self.user,
            password=self.password
        )
        print("Connection successful")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while connecting to database: {error}")


def disconnect(self):
    if self.connection:
        self.connection.close()
        print("Connection to database closed.")