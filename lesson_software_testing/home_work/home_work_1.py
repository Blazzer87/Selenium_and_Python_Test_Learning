import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://airgun.org.ru/forum/index.php')
time.sleep(3)                                           # таймер на 3 секунды чтобы увидеть станицу
driver.back()                                           # навигация назад
time.sleep(3)
driver.forward()                                        # навигация вперёд
time.sleep(3)
driver.refresh()                                        # перезагрузка страницы
driver.refresh()                                        # перезагрузка страницы