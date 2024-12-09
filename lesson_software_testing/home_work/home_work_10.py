'''
Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.
Более точно, нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:

ГЛАВНЫЙ ЭКРАН:
1) регулярная цена ЗАЧЁРКНУТАЯ на главной странице
2) регулярная цена СЕРОГО цвета на главной странице (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
3) акционная цена ЖИРНАЯ на главной странице
4) акционная цена КРАСНОГО цвета на главной странице (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
5) акционная цена КРУПНЕЕ, чем обычная на главной странице

КАРТОЧКА ТОВАРА:
6) регулярная цена ЗАЧЁРКНУТАЯ на странице товара
7) регулярная цена СЕРОГО цвета на странице товара (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
8) акционная цена ЖИРНАЯ на странице товара
9) акционная цена КРАСНОГО цвета на странице товара (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
10) акционная цена КРУПНЕЕ, чем обычная на странице товара

ПРОВЕРКИ ОБОИХ ЭКРАНОВ:
11) текстовое название товара одинаковые на главной странице и на странице товара
12) регулярные цены товара одинаковые на обоих страницах
13) акционная цена товара одинаковые на главной странице и на странице товара


14) кроссбраузерность - (Chrome, Firefox, IE)
'''
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = ["Chrome", "Firefox", "Ie"]
x = 0

while x < len(browser):
    if x == 0:



        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        driver = webdriver.Chrome(options)
    elif x == 1:
        options = webdriver.FirefoxOptions()
        options.add_argument('start-maximized')
        driver = webdriver.Firefox(options)
    elif x == 2:
        driver = webdriver.Ie()

    driver.get('http://localhost/litecart/en/')
    driver.implicitly_wait(2)

    # нашли первую утку в блоке Кампейнс
    first_campaigns_utka = driver.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]')

    # ДЛЯ ПРОВЕРОК №11-12-13
    # нашли имя у найденной утки
    name_main_page = first_campaigns_utka.find_element(By.XPATH, '//*[@id="box-campaigns"]/div/ul/li[1]/a[1]/div[2][text()]').text
    # находим регулярную цену на главной странице
    regular_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s[text()]').text
    # находим акционную цену на главной странице
    campaign_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//strong[text()]').text

    # проверка №1 - регулярная цена зачёркнутая на главной странице
    # определяем тег регулярной цены на главной странице
    crossout_regular_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s').get_attribute('tagName')
    try:
        assert crossout_regular_price_main_page == 'S'
        print('Проверка №1 пройдена успешно - регулярная цена зачёркнутая на главной странице')
    except AssertionError:
        print('Не пройдена проверка №1 - регулярная цена зачёркнутая на главной странице')

    # проверка №2 - регулярная цена на главной странице серого цвета
    # определяем цвет регулярной цены на главной странице
    color_regular_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s[text()]').value_of_css_property('color')
    try:
        color_list = re.findall(r'\d+', color_regular_price_main_page)
        assert color_list[0] == color_list[1] == color_list[2]
        print('Проверка №2 пройдена успешно - регулярная цена на главной странице серого цвета')
    except AssertionError:
        print('Не пройдена проверка №2 - регулярная цена на главной странице серого цвета')

    # проверка №3 - акционная цена ЖИРНАЯ на главной странице
    # определяем тег акционной цены на главной странице
    bold_campaign_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//strong').get_attribute('tagName')
    try:
        assert bold_campaign_price_main_page == 'STRONG'
        print('Проверка №3 пройдена успешно - акционная цена ЖИРНАЯ на главной странице')
    except AssertionError:
        print('Не пройдена проверка №3 - акционная цена ЖИРНАЯ на главной странице')

    # проверка №4 - акционная цена КРАСНОГО цвета на главной странице
    # определяем цвет акционной цены на главной странице
    color_campaign_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//strong[text()]').value_of_css_property("color")
    try:
        color_list = re.findall(r'\d+', color_campaign_price_main_page)
        assert int(color_list[1]) == 0 and int(color_list[2]) == 0
        print('Проверка №4 пройдена успешно - акционная цена КРАСНОГО цвета на главной странице')
    except AssertionError:
        print('Не пройдена проверка №4 - акционная цена КРАСНОГО цвета на главной странице')

    # проверка №5 - акционная цена КРУПНЕЕ, чем обычная на главной странице
    # определим размеры регулярной и акционной цены на главной странице
    font_campaign_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//strong[text()]').value_of_css_property("font-size")
    font_regular_price_main_page = first_campaigns_utka.find_element(By.XPATH, '//div[@id="box-campaigns"]//li[@class="product column shadow hover-light"][1]//s[text()]').value_of_css_property('font-size')
    try:
        font_campaign_price_main_page_list = re.findall(r'\d+', font_campaign_price_main_page)  # паттерн \d+ возвращает целые числа
        font_regular_price_main_page_list = re.findall(r'\d+\.?\d', font_regular_price_main_page)  # паттерн \d+\.?\d возвращает дробные значения с разделителем точкой
        assert font_campaign_price_main_page_list[0] > font_regular_price_main_page_list[0]
        print('Проверка №5 пройдена успешно - акционная цена КРУПНЕЕ, чем обычная на главной странице')
    except AssertionError:
        print('Не пройдена проверка №5 - акционная цена КРУПНЕЕ, чем обычная на главной странице')

    # переходим в карточку товара
    first_campaigns_utka.click()

    # проверка №6 - регулярная цена зачёркнутая на странице товара
    # определяем тег регулярной цены на странице товара
    crossout_regular_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//s').get_attribute('tagName')
    try:
        assert crossout_regular_price_product_page == 'S'
        print('Проверка №6 пройдена успешно - регулярная цена зачёркнутая на странице товара')
    except AssertionError:
        print('Не пройдена проверка №6 - регулярная цена зачёркнутая на странице товара')

    # проверка №7 - регулярная цена на главной странице серого цвета
    # определяем цвет регулярной цены на странице товара
    color_regular_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//s[@class="regular-price"]').value_of_css_property('color')
    try:
        color_list = re.findall(r'\d+', color_regular_price_product_page)
        assert color_list[0] == color_list[1] == color_list[2]
        print('Проверка №7 пройдена успешно - регулярная цена на главной странице серого цвета')
    except AssertionError:
        print('Не пройдена проверка №7 - регулярная цена на главной странице серого цвета')

    # проверка №8 - акционная цена ЖИРНАЯ на главной странице
    # находим акционную цену на странице товара
    bold_campaign_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//strong[@class="campaign-price"]').get_attribute('tagName')
    try:
        assert bold_campaign_price_product_page == 'STRONG'
        print('Проверка №8 пройдена успешно - акционная цена ЖИРНАЯ на главной странице')
    except AssertionError:
        print('Не пройдена проверка №8 - акционная цена ЖИРНАЯ на главной странице')

    # проверка №9 - акционная цена КРАСНОГО цвета на странице товара
    # определяем цвет акционной цены на странице товара
    color_campaign_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//strong[@class="campaign-price"]').value_of_css_property("color")
    try:
        color_list = re.findall(r'\d+', color_campaign_price_product_page)
        assert int(color_list[1]) == 0 and int(color_list[2]) == 0
        print('Проверка №9 пройдена успешно - акционная цена КРАСНОГО цвета на странице товара')
    except AssertionError:
        print('Не пройдена проверка №9 - акционная цена КРАСНОГО цвета на странице товара')

    # проверка №10 - акционная цена КРУПНЕЕ, чем обычная на странице товара
    # определяем размеры регулярной и акционной цены на странице товара
    font_campaign_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//strong[@class="campaign-price"]').value_of_css_property("font-size")
    font_regular_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//s[@class="regular-price"]').value_of_css_property('font-size')
    try:
        font_campaign_price_product_page_list = re.findall(r'\d+', font_campaign_price_main_page)  # паттерн \d+ возвращает целые числа
        font_regular_price_product_page_list = re.findall(r'\d+\.?\d', font_regular_price_main_page)  # паттерн \d+\.?\d возвращает дробные значения с разделителем точкой
        assert font_campaign_price_product_page_list[0] > font_regular_price_product_page_list[0]
        print('Проверка №10 пройдена успешно - акционная цена КРУПНЕЕ, чем обычная на странице товара')
    except AssertionError:
        print('Не пройдена проверка №10 - акционная цена КРУПНЕЕ, чем обычная на странице товара')

    # проверка №11 - наименования товара одинаковые на обоих страницах
    # находим название утки на странице карточки товара
    name_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//h1').text
    try:
        assert name_product_page == name_main_page
        print('Проверка №11 пройдена успешно - наименования товара одинаковые на обоих страницах')
    except AssertionError:
        print('Не пройдена проверка №11 - наименования товара одинаковые на обоих страницах')

    # проверка №12 - регулярные цены товара одинаковые на обоих страницах
    # находим регулярную цену на странице карточки товара
    regular_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//s[@class="regular-price"]').text
    try:
        assert regular_price_product_page == regular_price_main_page
        print('Проверка №12 пройдена успешно - регулярные цены товара одинаковые на обоих страницах')
    except AssertionError:
        print('Не пройдена проверка №12 - регулярные цены товара одинаковые на обоих страницах')

    # проверка №13 - акционные цены товара одинаковые на обоих страницах
    # находим акционную цену на странице карточки товара
    campaign_price_product_page = driver.find_element(By.XPATH, '//div[@id="box-product"]//strong[@class="campaign-price"]').text
    try:
        assert campaign_price_product_page == campaign_price_main_page
        print('Проверка №13 пройдена успешно - акционные цены товара одинаковые на обоих страницах')
    except AssertionError:
        print('Не пройдена проверка №13 - акционные цены товара одинаковые на обоих страницах')

    print('\n')
    if x == 0:
        print("Завершены тесты на Chrome")
    elif x == 1:
        print("Завершены тесты на Firefox")
    elif x == 2:
        print("Завершены тесты на Internet Explorer")
    print('\n')
    x += 1
    driver.quit()

driver.quit()