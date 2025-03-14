import allure
import pytest

from pages.login_page import LoginPage
from resources.urls import LOGIN_URL, ORDER_HISTORY, MAIN_PAGE


class TestAccount:

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_profile_login(self, browser):
        browser.get(MAIN_PAGE)
        login_page = LoginPage(browser)
        login_page.click_button_account()

    @pytest.mark.parametrize(
        'email, password', [
            ["Vika_Pavlova_17@yandex.ru", "123456"]
        ]
    )
    @allure.title('Переход в раздел "История заказов"')
    def test_go_to_section_Order_History(self, browser, email, password):
        browser.get(LOGIN_URL)
        login_page = LoginPage(browser)
        login_page.open_history_orders(email, password)

        assert login_page.get_current_url() == ORDER_HISTORY

    @pytest.mark.parametrize(
        'email, password', [
            ["Vika_Pavlova_17@yandex.ru", "123456"]
        ]
    )
    @allure.title('Выход из аккаунта')
    def test_logout(self, browser, email, password):
        browser.get(LOGIN_URL)
        login_page = LoginPage(browser)
        login_page.logout(email, password)

        assert login_page.get_current_url() == LOGIN_URL
