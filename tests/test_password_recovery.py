import allure
import pytest

from pages.password_recovery_page import PasswordRecoveryPage
from resources.urls import FORGOT_PASS, LOGIN_URL


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_forgot_password(self, browser):
        browser.get(LOGIN_URL)
        password_recovery_page = PasswordRecoveryPage(browser)
        password_recovery_page.click_link_recovery()

        assert password_recovery_page.get_current_url() == FORGOT_PASS

    @pytest.mark.parametrize(
        'email', [
            "Vika_Pavlova_17@yandex.ru"
        ]
    )
    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_recovery_pass(self, browser, email):
        browser.get(FORGOT_PASS)
        password_recovery_page = PasswordRecoveryPage(browser)
        password_recovery_page.click_button_recovery(email)

        assert password_recovery_page.is_password_field_present()

    @pytest.mark.parametrize(
        'email', [
            "Vika_Pavlova_17@yandex.ru"
        ]
    )
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_view_pass_active(self, browser, email):
        browser.get(FORGOT_PASS)
        password_recovery_page = PasswordRecoveryPage(browser)
        password_recovery_page.click_button_recovery(email)

        parent_class_before_toggle = password_recovery_page.get_parent_class_password_field()
        password_recovery_page.toggle_password_visibility()
        active_class_after_toggle = password_recovery_page.get_parent_class_password_field()

        assert parent_class_before_toggle != active_class_after_toggle
