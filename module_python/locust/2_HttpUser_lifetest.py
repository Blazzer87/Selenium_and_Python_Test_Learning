from locust import HttpUser, task, constant


class ReestrTestUser(HttpUser):

    host = 'https://reestr-hello-api-linux.qpdev.ru'
    wait_time = constant(1)


    @task
    def get_authorize_methods(self):
        response = self.client.get(url='/api/v1/internal/authorization/user/get_authorize_methods')


    @task
    def sign_in(self):
        response = self.client.post(url='/api/v1/internal/authorization/user/sign_in',
                                 json={'phone': "79507586687", 'password': "!QAZ1qaz"})
        print(response.json())