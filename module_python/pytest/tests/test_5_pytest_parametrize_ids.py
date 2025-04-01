import pytest

class TestNum:



    @pytest.mark.parametrize("num", [1,2,3,2,5])
    def test_1(self, num):
        self.num = num
        quadro_num = self.num * self.num
        sum_num = self.num + self.num
        assert quadro_num == sum_num, "Произведение чисел и их сумма не равны"




    @pytest.mark.parametrize("num1, num2", [(1,2),(2,2),(3,2)], ids=['test1', 'test2', 'test3'])
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
    def test_3(self, username, password):
        # Тест логина с заданными учетными данными
        pass



    @pytest.mark.parametrize("test_input, expected", [
        ("3+5", 8),
        ("2+4", 6),
        pytest.param("6*9", 42, marks=pytest.mark.xfail)])      # заведомо битый тест помечается как xfail
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected




    @pytest.mark.parametrize("test_input,expected",[
        ("3+5", 8),
        pytest.param("1+7", 8, marks=pytest.mark.basic),
        pytest.param("2+4", 6, marks=pytest.mark.basic, id="basic_2+4"),
        pytest.param("6*9", 42, marks=[pytest.mark.basic, pytest.mark.xfail], id="basic_6*9"),
        ],
    )
    def test_eval_2(self, test_input, expected):
        assert eval(test_input) == expected