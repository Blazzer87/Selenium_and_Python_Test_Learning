# test_class.py

import pytest

class TestExample:

    @classmethod
    def setup_class(cls):
        print("\nПРОВЕРКА ЗАПУСКА В КЛАССЕ ПЕРЕД ТЕСТАМИ.")

    @classmethod
    def teardown_class(cls):
        print("\nПРОВЕРКА ЗАПУСКА В КЛАССЕ ПОСЛЕ ВСЕХ ТЕСТОВ")

    def test_example_1(self):
        assert True

    def test_example_2(self):
        assert True
