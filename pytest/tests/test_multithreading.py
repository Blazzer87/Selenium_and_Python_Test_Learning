import datetime
import pytest
import time

@pytest.mark.parametrize('i', range(2))
def test_one(i):
    time.sleep(4)
    assert True

@pytest.mark.parametrize('i', range(2))
def test_two(i):
    time.sleep(4)
    assert True

@pytest.mark.parametrize('i', range(2))
def test_three(i):
    time.sleep(4)
    assert True

@pytest.mark.parametrize('i', range(2))
def test_four(i):
    time.sleep(4)
    assert True

@pytest.mark.parametrize('i', range(2))
def test_five(i):
    time.sleep(4)
    assert True

# запуск через -  pytest -n 5 test_multithreading.py
