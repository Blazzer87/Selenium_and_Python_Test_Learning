'''
Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на главной странице.
Стикеры -- это полоски в левом верхнем углу изображения товара, на которых написано New или Sale или что-нибудь другое.
Сценарий должен проверять, что у каждого товара имеется ровно один стикер.
'''

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/en/')
driver.implicitly_wait(2)

product_list = driver.find_elements(By.CSS_SELECTOR, 'li.product')      # поместим всех уток в список
x = 0
while x < len(product_list):        # запустим цикл который будет равен числу карточек товара с утками
    try:
        sticker_list = product_list[x].find_elements(By.CSS_SELECTOR, 'div.sticker')        # ищем стикер только внутри карточки утки, перебирая каждую карточку из списка
        print(f'На {x+1} уточке размещён {len(sticker_list)} стикер')
        x += 1
    except NoSuchElementException:
        print(f'На {x + 1} уточке нет стикера')
        continue

driver.quit()