import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('https://fuji-san.ru/japonskie-sladosti')
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 8)

# находим прячущийся элемент
sort_element = driver.find_element(By.XPATH, '//div[@class="sorting-selection"]/ul[@class="menu-v sorting"]')
# лезем в его свойства, ищем свойство дисплей
display = sort_element.value_of_css_property('display')
# по умолчанию свойство дисплей = none
if display == 'none':
    # через java script присваиваем принудительльно свойству дисплей значение блокед, теперь он не прячется
    driver.execute_script("arguments[0].style.display = 'block';", sort_element)
# находим используя ожидание кнопку с текстом цена и тыкаем в неё
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sorting-selection"]//a[text()="Цена"]'))).click()

time.sleep(10)
driver.quit()