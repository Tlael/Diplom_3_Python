import allure

from pages.main_page import MainPage
from resources.locators import DETAILS_ING
from resources.urls import MAIN_PAGE, ORDER_FEED, LOGIN_URL


class TestBasicFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_to_go_click_constructor(self, browser):
        browser.get(LOGIN_URL)
        main_page = MainPage(browser)
        main_page.go_to_constructor()

        assert main_page.get_current_url() == MAIN_PAGE

    @allure.title('Переход по клику на «Лента заказов»')
    def test_to_go_click_order_feed(self, main_page):
        main_page.go_to_order_feed()

        assert main_page.get_current_url() == ORDER_FEED

    @allure.title('Всплывающее окно с деталями, если кликнуть на ингредиент')
    def test_popup(self, main_page):
        main_page.open_popup()

        details_text = main_page.wait_for_visibility(DETAILS_ING).text
        assert details_text == 'Детали ингредиента'

    @allure.title('Закрывание кликом по крестику всплывающего окна')
    def test_popup_closed(self, main_page):
        main_page.open_popup()
        main_page.wait_for_visibility(DETAILS_ING)
        main_page.close_popup()
        main_page.wait_until_invisible(DETAILS_ING)

        assert not main_page.is_visible(DETAILS_ING)

    @allure.title('Увеличение каунтера ингредиента, при добавлении этого ингредиента в заказ')
    def test_drag_and_drop_fluorescent_bun(self, main_page):
        main_page.add_filling_to_order()

        num_ingredients = main_page.get_num_ingredients()
        assert num_ingredients > 0

    @allure.title('Оформление заказа залогиненным пользователем')
    def test_create_order_with_login_user(self, browser):
        browser.get(LOGIN_URL)
        main_page = MainPage(browser)
        main_page.profile_login()
        main_page.add_filling_to_order()
        main_page.click_create_order_button()

        order_text = main_page.get_order().text
        assert order_text == "Ваш заказ начали готовить"
