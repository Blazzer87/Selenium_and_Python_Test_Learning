



import warnings

def check_positive(x):
    if x < 0:
        warnings.warn("Negative value!", UserWarning)
    return x

print(check_positive(-10))

import pytest


def test_check_positive(recwarn):
    # Вызовем функцию с отрицательным значением
    result = check_positive(-1)

    # Проверим, что предупреждение было вызвано
    assert len(recwarn) == 1  # Должно быть одно предупреждение
    assert recwarn[0].category == UserWarning  # Тип предупреждения
    assert str(recwarn[0].message) == "Negative value!"  # Сообщение предупреждения
