import pytest


@pytest.fixture
def create_user():
    pass

# ЗАПУСК ФИКСТУРНОЙ ФУНКЦИИ С УКАЗАНИЕМ ЭТО САМОЙ ФУНКЦИИ
@pytest.mark.usefixtures("create_user")
def update_user():
    pass



# автозапуск функции
@pytest.fixture(autouse=True)
def setup():
    pass


# разделение функции на две части - предусловие и постусловие, а тесты в середине - используется генератор yield
@pytest.fixture(autouse=True)
def setup_2():
    x = 1
    yield
    del x


# НА ВЕСЬ ПРОГОН ТЕСТОВ
@pytest.fixture(scope="session")
def function_1():
    pass

# ТОЛЬКО НА ДАННУЮ ПАПКУ
@pytest.fixture(scope="package")
def function_2():
    pass

# ТОЛЬКО НА ДАННЫЙ ФАЙЛ
@pytest.fixture(scope="module")
def function_3():
    pass

# ТОЛЬКО НА ДАННУЮ ФУНКЦИЮ - ИСПОЛЬЗУЕТСЯ ПО ДЕФОЛТУ ЕСЛИ НЕ УКАЗАНО ЗНАЧЕНИЕ СКОУПА
@pytest.fixture(scope="function")
def function_4():
    pass

# ТОЛЬКО НА ДАННЫЙ КЛАСС
@pytest.fixture(scope="class")
def function_5():
    pass