# test_method.py

import pytest

class TestExample:

    def setup_method(self, method):
        print(f"\nПРОВЕРКА ЗАПУСКА ПЕРЕД выполнения метода {method.__name__}")

    def teardown_method(self, method):
        print(f"\nПРОВЕРКА ЗАПУСКА ПОСЛЕ выполнения метода {method.__name__}")

    def test_METHOD_1(self):
        assert True

    def test_METHOD_2(self):
        assert True

