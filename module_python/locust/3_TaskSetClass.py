from locust import User, task, between, TaskSet


class TestTaskSetClass(TaskSet):

    @task
    def get_method(self):

    @task
    def post_method(self):
        print('Post Method')


class Test234(User):

    wait_time = between(1,5)
    tasks = [TestTaskSetClass]







