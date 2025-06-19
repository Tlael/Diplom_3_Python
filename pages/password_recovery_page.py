import allure

from pages.base_page import BasePage
from resources.locators import FIELD_EMAIL, BUTTON_RECOVERY, LINK_RECOVERY_PASS, BUTTON_VIEW_PASS, \
    PASSWORD_FIELD_PARENT, FIELD_NEW_PASSWORD


class PasswordRecoveryPage(BasePage):
    @allure.step("Клик по ссылке Восстановить пароль")
    def click_link_recovery(self):
        self.click_button_account()
        self.wait_for_visibility(FIELD_EMAIL)
        link_recovery_pass = self.find_element(LINK_RECOVERY_PASS)
        self.driver.execute_script("arguments[0].click();", link_recovery_pass)

    @allure.step("Ввод email и клик по кнопке Восстановить")
    def click_button_recovery(self, email):
        self.find_element(FIELD_EMAIL).send_keys(email)
        button_recovery_pass = self.find_element(BUTTON_RECOVERY)
        self.driver.execute_script("arguments[0].click();", button_recovery_pass)

    @allure.step("Проверка наличия поля ввода Пароль")
    def is_password_field_present(self):
        field = self.find_element(FIELD_NEW_PASSWORD)
        return field.is_displayed()

    @allure.step("Нажимаем кнопку Показать/скрыть пароль")
    def toggle_password_visibility(self):
        button_view_pass = self.find_element(BUTTON_VIEW_PASS)
        self.driver.execute_script("arguments[0].click();", button_view_pass)

    @allure.step("Получаем родительский класс поля с паролем")
    def get_parent_class_password_field(self):
        return self.find_element(PASSWORD_FIELD_PARENT)
