"""Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.
Сценарий должен состоять из следующих частей:
1) зайти в админку
2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
3) открыть на редактирование какую-нибудь страну или начать создание новой
4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой -
- они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.
Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank".
Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне,
потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.
Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна."""

import random

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома
options.page_load_strategy = 'eager'                # меняем стратегию загрузки страницы на более раннюю - АДАПТАЦИЯ ТЕСТА ПОД ДЛИТЕЛЬНУЮ ЗАГРУЗКУ СТРАНИЦЫ 4
# options.add_argument('incognito')                   # передаём инкогнито в опции хрома
driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
driver.implicitly_wait(2)

username = driver.find_element(By.CSS_SELECTOR, '[name=username]')
username.send_keys('admin')
password = driver.find_element(By.CSS_SELECTOR, '[name=password]')
password.send_keys('admin')
rememberme = driver.find_element(By.CSS_SELECTOR, '[name=remember_me]')
rememberme.click()
submit = driver.find_element(By.CSS_SELECTOR, '[name=login]')
submit.click()

edit_country_list = driver.find_elements(By.XPATH, '//a[@title="Edit"]')        # на странице Кантри получаем весь список кнопок редактировать для кажой из стран
random_edit_country = random.choice(edit_country_list)        # выбираем случайную страну из списка
random_edit_country.click()

link_button_list = driver.find_elements(By.XPATH, '//form[@method="post"]//a[@target="_blank"]')        # все кнопки со ссылками на внешние ресурсы получаем в список

elements_locator_dict = {
    'iso_code_2':'//td[./input[@name="iso_code_2"]]/a[@target="_blank"]',
    'iso_code_3':'//td[./input[@name="iso_code_3"]]/a[@target="_blank"]',
    'tax_id_format':'//td[./input[@name="tax_id_format"]]/a[@target="_blank"]',
    'address_format':'//td[./textarea[@name="address_format"]]/a[@target="_blank"]',
    'postcode_format':'//td[./input[@name="postcode_format"]]/a[@target="_blank"]',
    'currency_code':'//td[./input[@name="currency_code"]]/a[@target="_blank"]',
    'phone_code':'//td[./input[@name="phone_code"]]/a[@target="_blank"]'
}                   # создаём словарь с локаторами по каждой из кнопок, где ключ - название, а кнопки - значение XPATH локатор

main_window = driver.current_window_handle          # определяем текущую страницу как главную

for i in range(len(link_button_list)):         # запускаем цикл, равный количеству табов с внешней ссылкой
    link = driver.find_element(By.XPATH, f'{list(elements_locator_dict.values())[i]}')      # таб определяется по локатору из словаря, обращаемся к значению словаря переводя его в список, где индекс равен номеру цикла.
    link.click()
    wait = WebDriverWait(driver, 8)
    wait.until(expected_conditions.number_of_windows_to_be(2))           # ждём пока открытых страниц станет 2
    all_window_list = driver.window_handles                    # все открытые страницы определяем в список
    for window_for_open_link in all_window_list:              # перебираем список с идентификаторами страниц
        if window_for_open_link != main_window:             # определяем новую открытую страницу
            driver.switch_to.window(window_for_open_link)           # переключаемся в новую страницу
            all_window_list.remove(window_for_open_link)            # удаляем из списка страниц страницу с внешней ссылкой, список вновь состоит из с траница = главной
            break
    try:
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//h1')))       # ждём пока на открывшейся странице обнаружится заголовок страницы
        h1 = driver.find_element(By.XPATH, '//h1')              # находим текстовый заголовок страницы
        print(f"Успешно открыта страница {h1.text}.")
    except TimeoutException:
        print(f"Возникла ошибка при загрузке страницы.")
    finally:
        driver.close()              # закрываем новое окно
        driver.switch_to.window(main_window)        # переключаемся на главный экран
print("Проверка завершена.")
driver.quit()
