import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def start_driver():
    options = webdriver.ChromeOptions()  # создаём опции хрома
    options.add_argument('start-maximized')  # передаём фулскрин в опции хрома
    options.add_argument('incognito')  # передаём инкогнито в опции хрома
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options)
    return driver


class BasePage:

    def __init__(self):
        driver = start_driver()
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

    def open(self, url):
        self.driver.get(url)

    def __del__(self):
        self.driver.close()

class Links:

    text_box = "https://demoqa.com/text-box"


class Page1TextBox (BasePage):

    URL = Links.text_box

    text_box_locator = (By.XPATH, '//span[text()="Text Box"]')
    full_name_locator = (By.XPATH, '//input[@id="userName"]')
    email_locator = (By.XPATH, '//input[@id="userEmail"]')
    current_address_locator = (By.XPATH, '//textarea[@id="currentAddress"]')
    permanent_address_locator = (By.XPATH, '//textarea[@id="permanentAddress"]')
    submit_button_locator = (By.XPATH, '//button[@id="submit"]')
    test_field_locator = (By.XPATH, '//div[@class="output"]')

    def enter_full_name(self, full_name):
        self.wait.until(EC.element_to_be_clickable(self.full_name_locator)).send_keys(full_name)


    def enter_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)


class BaseTest:

    x = Page1TextBox()


class Test1(BaseTest):

    def test_text_box(self):
        self.x.open(self.x.URL)
        self.x.enter_full_name('gfdgdfgdfgfgsfgdsgf')
        self.x.enter_email('gdsgfdsgdfgertqewrtewrewrewr')
        time.sleep(2)