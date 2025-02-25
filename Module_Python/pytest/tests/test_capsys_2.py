import sys
import pytest


def divide(a, b):
    if b == 0:
        print("Error: Division by zero!", file=sys.stderr)
        return None
    return a / b

        # тест потока ошибок
def test_divide_by_zero(capsys):
    result = divide(10, 0)

    # Захватим вывод
    captured = capsys.readouterr()

    # Проверим результат
    assert result is None
    assert captured.out == ""
    assert captured.err == "Error: Division by zero!\n"

        # тест потока вывода
def test_divide_positive(capsys):
    result = divide(10, 2)
    print(result)               # принт обязателен чтобы ассертить не только result, но и стандартный поток вывода
    # Захватим вывод
    captured = capsys.readouterr()

    # Проверим результат
    assert result == 5
    assert captured.out == "5.0\n"
    assert captured.err == ""
