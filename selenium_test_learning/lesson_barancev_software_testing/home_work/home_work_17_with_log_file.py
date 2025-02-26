from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_and_send_keys (locator, input):
    field = driver.find_element(By.XPATH, f'{locator}')
    field.clear()
    field.send_keys(f'{input}')

def find_and_click (locator):
    tab = driver.find_element(By.XPATH, f'{locator}')
    tab.click()

def autorization_by_admin():
    find_and_send_keys('//input[@name="username"]', "admin")
    find_and_send_keys('//input[@name="password"]', "admin")
    find_and_click('//input[@type="checkbox"][@name="remember_me"]')
    find_and_click('//button[@type="submit"]')


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument("--headless")                # безголовый режим
options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})

# Уровни логгирования (в порядке убывания детализации):
# Каждый уровень содержит свой уровень + те, что ниже его, но не содержит те что выше.
# ALL: Все сообщения. Выводит все сообщения независимо от уровня.
# DEBUG: Сообщения для дебаггинга.
# INFO: Сообщения информативного характера.
# WARNING: Предупреждения о том, что могло быть неверным, хоть ситуация и была успешно обработано.
# SEVERE: Сообщения об ошибках.
# OFF: Логгирование отключено.

driver = webdriver.Chrome(options)

driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=2')

autorization_by_admin()

product_row_list = driver.find_elements(By.XPATH, '//table[@class="dataTable"]//tr[@class="row"]/td[3]/a[contains(@href,"edit_product")]')
wait = WebDriverWait(driver,2)

for i in range(len(product_row_list)):
    product_row_list = driver.find_elements(By.XPATH,'//table[@class="dataTable"]//tr[@class="row"]/td[3]/a[contains(@href,"edit_product")]')
    product_row_list[i].click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//h1')))
    browser_logs = driver.get_log('browser')
    print("Логи браузера для страницы:", (driver.find_element(By.XPATH, '//h1')).text)
    for log in browser_logs:
        print(log)
        with open('home_work_17_log', "a+") as file:
            file.write(f'{datetime.now()}, {log} \n')
    print("\n")
    driver.back()

driver.quit()