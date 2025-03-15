import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from resources.urls import MAIN_PAGE, LOGIN_URL, FORGOT_PASS, ORDER_FEED


# Фикстуры для различных браузеров
@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def browser(request):
    driver = None
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(browser):
    browser.get(LOGIN_URL)
    return LoginPage(browser)


@pytest.fixture
def main_page(browser):
    browser.get(MAIN_PAGE)
    return MainPage(browser)


@pytest.fixture
def password_recovery_page(browser):
    browser.get(FORGOT_PASS)
    return PasswordRecoveryPage(browser)


@pytest.fixture
def order_feed_page(browser):
    browser.get(ORDER_FEED)
    return OrderFeedPage(browser)
