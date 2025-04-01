import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options


base_url = browser.config.base_url = "https://demoqa.com/automation-practice-form"

# Настройка размера окна браузера
@pytest.fixture()
def browser_config():
    options = Options()
    options.add_argument('--headles')
    options.add_argument('window_size = 1920, 1080')
    browser.config.driver_options = options

# Открытие страницы поисковика с настройками
@pytest.fixture()
def open_url(browser_config):

    browser.config.base_url = "https://demoqa.com"

    yield

    browser.quit()