import inspect
import re
import pytest
import requests



@pytest.fixture
def access_token():
    response = requests.post(url='http://192.168.100.17:18080/auth/realms/qpd/protocol/openid-connect/token',
                             headers={'Content-Type': 'application/x-www-form-urlencoded'},
                             data={'client_id': 'vdcs3-dev',
                                   'grant_type': 'password',
                                   'client_secret': 'xHUokMjWsrMuBIXugXFdrqvzVEbgvr',
                                   'username': 'vdcs3tst',
                                   'password': 'Co_ZLHb5ao'}
                             )
    return response.json()['access_token']


def create_user(role, obj_num, sub_obj_num):
    """ в этом блоке нужно создать пользователя"""
    """ в аргументах передать роль - user, tav_manager, tav_admin"""
    """ в аргументах передать номер объекта и подномер"""
    """ хардкодно зашивается имя - pmi-user-obj_num-sub_obj_num"""
    """ хардкодно зашивается пароль"""
    """ вернуть id пользователя"""
    pass


def create_vendor(num, sub_num, *args):
    response = requests.post(url='http://192.168.100.17:4000/api/context/v1/vendor',
                             headers={'Content-Type': 'application/json'}|{'Authorization': f'Bearer {access_token}'},
                             json={'code': f'pmi-vendor-{num}-{sub_num}', "subscribers": [args]}
                             )


class TestData:

    def test_method_23(self):

        """получаем номер метода"""
        obj_num = re.sub(r'[a-zA-Z_-]','',inspect.currentframe().f_code.co_name)

        """создание пользователя"""
        user1 = create_user('admin', obj_num=obj_num, sub_obj_num=1)
        user2 = create_user('admin', obj_num=obj_num, sub_obj_num=2)

        """создать вендора"""
        vendor1 = create_vendor(num=obj_num, sub_num=1)
        vendor2 = create_vendor

        #
        # создать кайнда
        #
        # создать вендора
        #
        # создать правило
        #
        # создать документ
        #
