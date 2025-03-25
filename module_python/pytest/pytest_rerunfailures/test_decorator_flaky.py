import pytest

"""обязателен pip install pytest-rerunfailures"""


@pytest.mark.flaky(reruns=5)                # Декоратор для повторного запуска теста
def test_flaky():
    if test_flaky.var < 4:
        test_flaky.var += 1
        assert test_flaky.var == 5

test_flaky.var = 0
