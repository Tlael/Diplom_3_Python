import allure

from pages.base_page import BasePage
from resources.locators import FIELD_EMAIL, FIELD_PASSWORD, BUTTON_HISTORY_ORDERS, BUTTON_LOGOUT_IN_PROFILE, \
    BUTTON_LOGIN

from resources.urls import PROFILE_URL, LOGIN_URL, MAIN_PAGE

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginPage(BasePage):

    @allure.step("Клик по кнопке История заказов")
    def click_button_history_orders(self):
        button_history = self.find_element(BUTTON_HISTORY_ORDERS)
        self.driver.execute_script("arguments[0].click();", button_history)

    @allure.step("Ввод данных для авторизации")
    def enter_credentials(self, email, password):
        self.find_element(FIELD_EMAIL).send_keys(email)
        self.find_element(FIELD_PASSWORD).send_keys(password)

    @allure.step("Авторизация в аккаунте")
    def login_in_account(self, email, password):
        self.enter_credentials(email, password)
        self.click_button_login()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(MAIN_PAGE)
        )

    @allure.step("Переход в профиль")
    def go_to_profile(self):
        self.click_button_account()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(PROFILE_URL)
        )

    @allure.step("Открытие истории заказов")
    def open_history_orders(self, email, password):
        self.login_in_account(email, password)
        self.go_to_profile()
        self.click_button_history_orders()

    @allure.step("Выход из аккаунта")
    def logout(self, email, password):
        self.login_in_account(email, password)
        self.go_to_profile()
        logout_link = self.find_element(BUTTON_LOGOUT_IN_PROFILE)
        self.driver.execute_script("arguments[0].click();", logout_link)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )

    @allure.step("Создание заказа")
    def create_order(self):
        self.add_filling_to_order()
        self.click_create_order_button()

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_button_login(self):
        login_link = self.find_element(BUTTON_LOGIN)
        self.safe_click(login_link)
