

def pytest_sessionstart(session):
    print("\n!!!!!!!!!!!!!!!Начало сессии тестирования - ЭТО ПРИМЕР ХУКА ДЛЯ СЕССИИ!!!!!!!!!!!! это  хук pytest_sessionstart!!!!!!!!!!!!!!!!!!!!он лежит в conftest")

def pytest_sessionfinish(session, exitstatus):
    print("\n!!!!!!!!!!!!!!!!!!!!!!Завершение сессии тестирования - ЭТО ПРИМЕР ХУКА ДЛЯ СЕССИИ!!!!!!!!!!!это хук pytest_sessionfinish!!!!!!!!!!!!!!он лежит в conftest")



def pytest_runtest_setup(item):
    print(f"\nНастройка для теста: {item.name} ЭТО ХУК pytest_runtest_setup")

def pytest_runtest_teardown(item, nextitem):
    print(f"\nОчистка после теста: {item.name} ЭТО ХУК pytest_runtest_teardown")