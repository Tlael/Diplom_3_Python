import allure

from pages.base_page import BasePage
from resources.locators import DETAILS_ING
from resources.urls import MAIN_PAGE, ORDER_FEED, LOGIN_URL


class TestBasicFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_to_go_click_constructor(self, browser):
        browser.get(LOGIN_URL)
        base_page = BasePage(browser)
        base_page.to_go_click_constructor()

        assert base_page.get_current_url() == MAIN_PAGE

    @allure.title('Переход по клику на «Лента заказов»')
    def test_to_go_click_order_feed(self, browser):
        browser.get(MAIN_PAGE)
        base_page = BasePage(browser)
        base_page.to_go_click_order_feed()

        assert base_page.get_current_url() == ORDER_FEED

    @allure.title('Всплывающее окно с деталями, если кликнуть на ингредиент')
    def test_popup(self, browser):
        browser.get(MAIN_PAGE)
        base_page = BasePage(browser)
        base_page.view_popup()

        details_text = base_page.wait_for_visibility_popup(DETAILS_ING).text
        assert details_text == 'Детали ингредиента'

    @allure.title('Закрывание кликом по крестику всплывающего окна')
    def test_popup_closed(self, browser):
        browser.get(MAIN_PAGE)
        base_page = BasePage(browser)
        base_page.view_popup()
        base_page.wait_for_visibility(DETAILS_ING)
        base_page.click_closed_popup()

        assert not base_page.wait_for_visibility(DETAILS_ING)

    @allure.title('Увеличение каунтера ингредиента, при добавлении этого ингредиента в заказ')
    def test_drag_and_drop_fluorescent_bun(self, browser):
        browser.get(MAIN_PAGE)
        base_page = BasePage(browser)
        base_page.add_filling_to_order()

        num_ingredients = base_page.get_num_ingredients()
        assert num_ingredients > 0

    @allure.title('Оформление заказа залогиненным пользователем')
    def test_create_order_with_login_user(self, browser):
        browser.get(LOGIN_URL)
        base_page = BasePage(browser)
        base_page.profile_login()
        base_page.add_filling_to_order()
        base_page.click_create_order_button()

        order_text = base_page.get_order().text
        assert order_text == "Ваш заказ начали готовить"
