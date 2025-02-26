import pytest
from contextlib import nullcontext as does_not_raises

class Calculator:

    def add (self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, int | float) or not isinstance(y, int | float):
            raise TypeError ("невалидный тип данных")
        return x + y


    def divide (self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, int | float) or not isinstance(y, int | float):
            raise TypeError ("невалидный тип данных")
        # if y == 0:
        #    raise ValueError("Делить на ноль нельзя")      закомментил чтобы работал обработчик ошибок
        return x / y

        # 1 ВАРИАНТ ОБРАБОТЧИК ОШИБОК

class TestCalculator:

    @pytest.mark.parametrize('x, y, result, expectation',
                             [(1, 1, 2, does_not_raises()),
                              (2, 2, 4, does_not_raises()),
                              (10, 5, 15, does_not_raises()),
                              (2222, "", 3333, pytest.raises(TypeError))]
                             )
    def test_add(self, x, y, result, expectation):
        with expectation:
            assert Calculator().add(x, y) == result

    @pytest.mark.parametrize('x, y, result, expected',
                             [(1, 1, 1, does_not_raises()),
                              (2, 2, 1, does_not_raises()),
                              (10, 5, 2, does_not_raises()),
                              (10, 0, 0, pytest.raises(ZeroDivisionError)),
                              (2222, "hello", 3333, pytest.raises(TypeError))]
                             )
    def test_divide(self, x, y, result, expected):
        with expected:
            assert Calculator().divide(x, y) == result

        # 2 ВАРИАНТ УПРОЩЁННЫЙ ОБРАБОТЧИК ОШИБОК

class Calculator2:

    def divide(self, x, y):
        return x / y

@pytest.mark.parametrize('x, y, expected_exception', [(1, 0, ZeroDivisionError),(10, "privet", TypeError)])
def test_divide_exceptions(x, y, expected_exception):
    with pytest.raises(expected_exception):
        Calculator2().divide(x, y)




"""
обработчик ошибок:
создаётся импорт - from contextlib import nullcontext as does_not_raises
в параметризацию передаётся 4-ый атрибут expectation
в кортежи данных передаются - или функции does_not_raises() или ожидание ошибки pytest.raises(TypeError)
в функцию добавляется 4ый атрибут expectation
функция выполняется внутри контекстного менеджера with expectation:
в итоге если получена ошибка которая и ожидалась - значит тест провалился как и ожидалось, тест успешно пройден
"""



"""
pytest
pytest -v
pytest pytest/tests/test_1_параметризация_обработчик_ошибок.py::test_3 - запуск отдельной функции
pytest pytest/tests/test_1_параметризация_обработчик_ошибок.py::TestCalculator - запускает всё в классе. Если класса нет то пишется функция
"""

