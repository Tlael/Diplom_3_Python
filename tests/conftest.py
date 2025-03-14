import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Фикстуры для различных браузеров
@pytest.fixture(params=['chrome', 'firefox'])
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
