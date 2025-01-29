from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')                 # развернуть браузер на весь экран
options.add_argument('incognito')                       # запуск в режиме инкогнито
options.add_argument("--deny-permission-prompts")       # запрет на выдачу запросов на разрешения (например о местоположении)
options.add_argument("--headless")                      # Запуск в фоновом режиме, без открытия браузера
options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})         # логирование браузера
options.add_argument("--ignore-certificate-errors")     # игнорим ошибки сертификатов если такие возникнут
options.add_argument("--disable-dev-shm-usage")       # актуально только при контейнеризации в докере для исключения дефицита объёма памяти


options.page_load_strategy = 'eager'                    # меняем стратегию загрузки страницы на более раннюю - Доступ к DOM готов, но другие ресурсы, такие как изображения, могут все еще загружаться
options.page_load_strategy = 'none'                     # меняем стратегию загрузки страницы на более раннюю - Не блокирует WebDriver вообще

options.add_experimental_option("excludeSwitches", ["enable-automation"])       # отключает уведолмени что вашим браузером управляет робот


# options.add_argument("--enable-logging")            # Включение логирования - НЕ СРАБОТАЛИ, перепроверять
# options.add_argument("--v=3")                       # Уровень логирования - НЕ СРАБОТАЛИ, перепроверять