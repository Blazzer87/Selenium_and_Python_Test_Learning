import pytest
import time

def pytest_addoption(parser):
    parser.addoption("--run-slow", action="store_true", help="run slow tests")

@pytest.mark.skipif(not pytest.config.getoption("--run-slow"), reason="Skipping slow test")
def test_slow_function():
    time.sleep(2)  # Симулируем медленный тест
    assert True

def test_fast_function():
    assert 1 + 1 == 2
