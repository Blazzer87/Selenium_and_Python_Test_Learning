import pytest


@pytest.mark.repeat(2)
def test_addition():
    assert 1 + 1 == 2


@pytest.mark.repeat(3)
def test_subtraction():
    assert 2 - 1 == 1


@pytest.mark.parametrize("input,expected", [(1, 2), (2, 3), (3, 4)])
@pytest.mark.repeat(2)
def test_increment(input, expected):
    assert input + 1 == expected



"""запуск через pytest test_module.py --count=10"""

"""
добавлении в опции в файл pytest.ini
[pytest]
addopts = --count=5"""