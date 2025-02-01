import pytest
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)            ## автоюс - автоматически внутри каждого теста, скоуп = фанкшен - создание экземляра браузера для каждого теста отдельно
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("--deny-permission-prompts")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options)
    request.cls.driver = driver
    yield driver
    driver.quit()