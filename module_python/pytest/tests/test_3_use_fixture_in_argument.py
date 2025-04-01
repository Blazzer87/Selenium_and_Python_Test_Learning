import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42


                                        # это пример как дёрнуть фикстуру через usefixture
@pytest.fixture()
def some_print():
    print("\nЭТО ФИКСТУРА И ОНА ЧТО ТО ВЫВОДИТ НА КОНСОЛЬ. эТО ДЛЯ ПРИМЕРА КАК СДЕЛАТЬ ЮСФИКТУР")

@pytest.mark.usefixtures("some_print")
def test_use_some_print():
    print("\n А ЭТО ТЕСТОВАЯ ФУНКЦИЯ КОТОРАЯ ДОЛЖНА ДЁРГАТЬ ЧЕРЕЗ ДЕКОРАТОР ФИКСТУРУ САМ_ПРИНТ")