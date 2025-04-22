import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True, scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)
    yield driver
    driver.quit()

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get("https://demoqa.com/radio-button")

class PageButton(BasePage):

    locator = ('xpath', '//label[@class="custom-control-label"]')

    def click_to_button(self):
        self.wait.until(EC.element_to_be_clickable(self.locator)).click()

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page10 = PageButton(driver)

class Test(BaseTest):

    def test(self):
        self.page10.open()
        self.page10.click_to_button()
        time.sleep(2)