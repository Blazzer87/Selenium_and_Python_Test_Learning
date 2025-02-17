import pytest

class TestNum:


    @pytest.mark.parametrize("num", [1,2,3,2,5])
    def test_1(self, num):
        self.num = num
        quadro_num = self.num * self.num
        sum_num = self.num + self.num
        assert quadro_num == sum_num, "Произведение чисел и их сумма не равны"


    @pytest.mark.parametrize("num1, num2",
                             [(1,2),(2,2),(3,2)]
                             )
    def test_2(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        quadro_num = self.num1 * self.num2
        sum_num = self.num1 + self.num2
        assert quadro_num == sum_num, "Произведение чисел и их сумма не равны"

    @pytest.mark.parametrize("username, password", [
        ("user1", "pass1"),
        ("user2", "pass2"),
        ("admin", "adminpass"),
    ], ids=["User One", "User Two", "Administrator"])
    def test_3(username, password):
        # Тест логина с заданными учетными данными
        pass