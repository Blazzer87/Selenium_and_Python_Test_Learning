import pytest

"""обязателен pip install pytest-rerunfailures"""


@pytest.mark.flaky(reruns=7)                # Декоратор для повторного запуска теста
def test_flaky():
    if test_flaky.var < 10:
        test_flaky.var += 1
        assert test_flaky.var == 10

test_flaky.var = 0

""" сравнение флаки и репита - репит будет делать тстолько прогонов сколько указано, 
    флаки же будет делать реран пока возвращается failed, если вернётся passed то останавливается"""


@pytest.mark.repeat(7)
def test_repeat():
    if test_flaky.var < 4:
        test_flaky.var += 1
        assert test_flaky.var == 5

test_flaky.var = 0
