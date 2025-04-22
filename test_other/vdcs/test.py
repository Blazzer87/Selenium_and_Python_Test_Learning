import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('--ignore-certificate-errors')  # Игнорировать ошибки сертификатов
options.add_argument('--allow-insecure-localhost')  # Разрешить небезопасный localhost
options.add_argument('--disable-blink-features=BlockCredentialedSubresources')
options.add_argument("--deny-permission-prompts")
driver = webdriver.Chrome(options)
wait = WebDriverWait(driver, 10)


def do_screenshot(screenshot_name=None):
    allure.attach(
            body=driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.JPG)


def test_vdcs():
    with allure.step("Открыть главную страницу"):
        driver.get("https://vdcs3tst:Co_ZLHb5ao@192.168.100.17:4003/auth/realms/qpd/protocol/openid-connect/auth?client_id=vdcs3&redirect_uri=https%3A%2F%2F192.168.100.17%3A4003%2Fvendors&response_type=code&scope=openid")
        do_screenshot()
    with allure.step("Ввести логин и пароль:"):
        wait.until(EC.element_to_be_clickable(('xpath', '//input[@id="username"]'))).send_keys('vdcs3tst')
        wait.until(EC.element_to_be_clickable(('xpath', '//input[@id="password"]'))).send_keys('Co_ZLHb5ao')
        do_screenshot()
    with allure.step("Авторизоваться с переходом в справочник Vendors:"):
        wait.until(EC.element_to_be_clickable(('xpath', '//input[@type="submit"]'))).click()
        do_screenshot()
    with allure.step("Кликнуть на кнопку Create"):
        wait.until(EC.element_to_be_clickable(('xpath', '//button[@class="vdcs3-icon-text-button"]'))).click()
        do_screenshot()
    with allure.step("В модальном окне создания записи Вендора попытаться сохранить запись не заполняя поля"):
        wait.until(EC.element_to_be_clickable(('xpath', '//button[contains(@type, "ant-btn-variant-solid")]'))).click()
        do_screenshot()
    with allure.step("Заполнить Code и попытаться сохранить"):
        wait.until(EC.element_to_be_clickable(('xpath', '//input[@name="code"]'))).send_keys('vendor1')
        wait.until(EC.element_to_be_clickable(('xpath', '//button[contains(@type, "ant-btn-variant-solid")]'))).click()
        do_screenshot()









    time.sleep(5)
    driver.quit()