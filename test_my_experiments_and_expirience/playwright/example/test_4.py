import pytest
from playwright.sync_api import Playwright, Page, Browser


@pytest.fixture(autouse=True, scope='session', params=["chromium", "firefox", "webkit"])
def browser(request, playwright: Playwright):
    browser_type = request.param
    browser: Browser = getattr(playwright, browser_type).launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(autouse=True, scope='session')
def context(request, browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(autouse=True, scope='session')
def page(context):
    page: Page = context.new_page()
    yield page
    page.close()


def test_1(page):
    page.goto("https://demoqa.com/text-box", wait_until='domcontentloaded')
