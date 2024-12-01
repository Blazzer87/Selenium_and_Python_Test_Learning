'''Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
1) входит в панель администратора http://localhost/litecart/admin
2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
'''


from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                 # создаём опции хрома
options.add_argument('start-maximized')             # передаём фулскрин в опции хрома

driver = webdriver.Chrome(options)                  # запускаем хром с опциями переданными ранее

driver.get('http://localhost/litecart/admin/login.php')

username = driver.find_element(By.CSS_SELECTOR, '[name=username]')
username.send_keys('admin')
password = driver.find_element(By.CSS_SELECTOR, '[name=password]')
password.send_keys('admin')
rememberme = driver.find_element(By.CSS_SELECTOR, '[name=remember_me]')
rememberme.click()
submit = driver.find_element(By.CSS_SELECTOR, '[name=login]')
submit.click()

ul_element = driver.find_element(By.CSS_SELECTOR, '#box-apps-menu.list-vertical')       # найдём весь элемент меню на странице
ul_child_count = ul_element.get_property("childElementCount")           # через свойства объекта определим количество дочерних элементов и поместим в переменную

x = 0
y = 1
while x < ul_child_count:       # если х меньше чем кол-во дочерних элементов то запускаем цикл
    ul_child_element = driver.find_elements(By.ID, 'app-')          # получаем все элементы меню в список
    ul_child_element[x].click()             # начинаем перебор списка
    # current_title = driver.title          # альтернативный вариант нахождения заголовка на странице
    current_title = driver.find_element(By.CSS_SELECTOR, 'h1')          # найдем заголовок
    print(current_title.text)               # выведем на экран в текстовом формате
    x += 1
    try:                                    # исключение для проверки есть ли у элемента подсписок
        docs_element = driver.find_element(By.CSS_SELECTOR, '.docs')          # если подсписок находится
        docs_child_count = docs_element.get_property("childElementCount")           # определяем длинну подсписка
        while y < docs_child_count:         # запускаем цикл для перебора подсписка
            docs_child_element = driver.find_elements(By.CSS_SELECTOR, '[id ^=doc]')        # находим все элементы подсписка по единообразному началу айдишника
            docs_child_element[y].click()           # перебираем элементы подсписка и прокликиваем
            # current_title = driver.title          # альтернативный вариант нахождения заголовка на странице
            current_title = driver.find_element(By.CSS_SELECTOR, 'h1')      # найдем заголовок
            print(current_title.text)           # выведем на экран в текстовом формате
            y += 1
        y = 1
    except NoSuchElementException:          # если у элемента подсписок не найден, то обрабатываем исключение
        continue
driver.quit()