from locust import User, task


class TestUser(User):

    @task
    def user1(self):
        print("Подключаемся 1")

    @task
    def user2(self):
        print("Подключаемся 2")


