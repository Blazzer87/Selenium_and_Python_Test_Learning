import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

text_box_locator = (By.XPATH, '//span[text()="Text Box"]')



class Links:

    PageTextBoxUrl = "https://demoqa.com/text-box"


def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)
    return driver


class BasePage:

    def __init__(self):
        self.driver = driver()
        self.wait = WebDriverWait(self.driver, 20)

    def open_page(self, url):
        self.driver.get(url)

    def close_driver(self):
        self.driver.close()

class PageTextBox(BasePage):

    url = Links.PageTextBoxUrl

    fullname_locator = (By.XPATH, '//input[@id="userName"]')


    def enter_fullname (self, fullname):
        self.wait.until(EC.element_to_be_clickable(self.fullname_locator)).send_keys(fullname)


class BaseTest:

    page : PageTextBox()

    def setup(self):

        self.page = PageTextBox()

class TestTextBox (BaseTest):

    def test_text_box(self):
        self.page.open_page(self.page.url)
        self.page.enter_fullname("dfsdfdsfagrearg")
        self.page.close_driver()




