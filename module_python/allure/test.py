import random

from allure_commons.types import AttachmentType
from selenium import webdriver


import allure
import pytest


@allure.epic("SUM - это allure.epic")
@allure.feature("Складываем - это allure.feature")
@allure.story("Правильно - allure.story")
@allure.title("test_1 - это тайтл и здесь ещё есть ids")
@pytest.mark.parametrize('x, y, expect', [
    (2,2,4),
    (3,3,6),
    (4,4,9),
],
                         ids=["this is ids= in pytest 2,2,4",
                              "this is ids= in pytest 3,3,6",
                              "this is ids= in pytest 4,4,9"]
                         )
def test_1(x, y, expect):
    assert expect == x + y


@allure.epic("SUM - это allure.epic")
@allure.feature("Складываем - это allure.feature")
@allure.story("Не правильно - allure.story")
@allure.title("test_2 - это тайтл и здесь ещё есть ids")
@pytest.mark.parametrize('x, y, expect', [
    (1,2,5)
],
                         ids=["this is ids= in pytest"]
                         )
def test_2(x, y, expect):
    assert expect == x + y


@allure.epic("SUM - это allure.epic")
@allure.feature("Вычитаем - это allure.feature")
@allure.story("Правильно - allure.story")
@allure.title("test_3 - это тайтл")
@allure.tag("tag1","tag2", "tag3")
@allure.description("Так работает allure.description")
@pytest.mark.parametrize('x, y, expect', [
    (6,2,4),
])
def test_3(x, y, expect):
    assert expect == x - y

@allure.epic("SUM - это allure.epic")
@allure.feature("Просто сравниваем, это другая фича - это allure.feature")
@allure.story("Должна быть ошибка - allure.story")
@allure.title("test_4 - это тайтл")
@allure.description("так настроено что он вечно падает - это дискрипшн")
@allure.tag("tag1","tag2", "tag3")
@allure.id("это декоратор - allure.id")
@allure.label("это декоратор - allure.label")
@allure.manual("это декоратор - allure.manual")
@allure.severity('произвольный mega-severity')
@allure.link('https://google.com')
def test_4():
    assert False

@allure.epic("SUM - это allure.epic")
@allure.feature("Просто сравниваем, это другая фича - это allure.feature")
@allure.story("Должна быть ошибка - allure.story")
@allure.title("test_5 - это тайтл ")
@allure.description("длинный много шаговый тест - это дискрипшн")
@allure.tag("tag1","tag2", "tag3")
@allure.id("это декоратор - allure.id")
@allure.label("это декоратор - allure.label")
@allure.manual("это декоратор - allure.manual")
@allure.severity(allure.severity_level.BLOCKER)
@allure.link('https://google.com')
def test_5(screenshot_name=None):
    driver = webdriver.Chrome()
    with allure.step('проверим 1+1 - это allure.step внутри теста'):
        assert 1 + 1 == 2
        driver.get("https://example.com/")
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.JPG)
    with allure.step('проверим 2+2 - это allure.step внутри теста'):
        driver.get("https://example.com/")
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.JPG)
        assert 2 + 2 == 4
    with allure.step('проверим щаг с заведомой ошибкой - это allure.step внутри теста'):
        driver.get("https://example.com/")
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.JPG)
        driver.quit()
        assert False


@pytest.fixture()
def fixtura_1():
    return random.randint(1, 5)


@allure.epic("SUM - это allure.epic")
@allure.feature("Просто сравниваем, это другая фича - это allure.feature")
@allure.story("50/50 ошибка или успех - allure.story")
@allure.step("Так работает allure.step в качестве декоратора к мини-функции")
@allure.severity(allure.severity_level.BLOCKER)
@allure.tag("tag1","tag2", "tag3")
@allure.id("это декоратор - allure.id")
@allure.label("это декоратор - allure.label")
@allure.manual("это декоратор - allure.manual")
@allure.link('https://google.com')
@pytest.mark.flaky(reruns=7)
def test_6(fixtura_1):
    assert fixtura_1 == 5