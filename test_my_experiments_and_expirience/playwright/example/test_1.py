import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pytest_playwright.pytest_playwright import device


@pytest.fixture(autouse=True, scope="function")
def page(playwright: Playwright):
        # запускает браузер с опциями
        # какие ещё опции есть - узнать
        browser = playwright.chromium.launch(headless=False, slow_mo=100, timeout=60000, devtools=True)
        # где headless - безголовый режим
        # где slow_mo - замедление действий
        # timeout время ожидания открытия страницы = 60 секунд = 60000 миллисекунд

        # создает изолированный сеанс браузера (новый объект окна браузера)
        context = browser.new_context()

        # создает страницу браузера в рамках этого изолированного сеанса
        page = context.new_page()

        yield page

        context.close()
        browser.close()


def test_1(page):

        # передаёт в страницу какой урл нам необходимо открыть
        page.goto("https://demoqa.com/text-box",
                  wait_until='commit',
                  timeout=50000,

                  )
        # где wait_until='domcontentloaded' - один из вариантов ожидания ранней загрузки страницы

        # действие передачи текста по объекту который найден через РОЛЬ
        page.get_by_role("textbox", name="Full Name").fill("Sergey")

        # действие передачи текста по объекту который найден через ЛОКАТОР
        page.locator("#permanentAddress").fill("и тут тоже какой то адрес")

        # действие передачи нажатия клавиши в объект который найден через ЛОКАТОР
        page.locator("#permanentAddress").press("Enter")


        page.get_by_role("textbox", name="Current Address").fill("павапвап")


