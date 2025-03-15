import allure

from pages.password_recovery_page import PasswordRecoveryPage
from resources.data_user import EMAIL
from resources.urls import FORGOT_PASS, LOGIN_URL


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_forgot_password(self, browser):
        browser.get(LOGIN_URL)
        password_recovery_page = PasswordRecoveryPage(browser)
        password_recovery_page.click_link_recovery()

        assert password_recovery_page.get_current_url() == FORGOT_PASS

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_recovery_pass(self, password_recovery_page):
        password_recovery_page.click_button_recovery(EMAIL)

        assert password_recovery_page.is_password_field_present()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_view_pass_active(self, password_recovery_page):
        password_recovery_page.click_button_recovery(EMAIL)

        parent_class_before_toggle = password_recovery_page.get_parent_class_password_field()
        password_recovery_page.toggle_password_visibility()
        active_class_after_toggle = password_recovery_page.get_parent_class_password_field()

        assert parent_class_before_toggle != active_class_after_toggle
