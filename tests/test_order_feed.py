import allure

from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from resources.locators import TOTAL_COUNT_TODAY
from resources.urls import LOGIN_URL


class TestOrderFeed:

    @allure.title('Всплывающее окно с деталями, при клике на заказ')
    def test_pop_with_details_order(self, order_feed_page):
        order_feed_page.navigate_to_order_feed()
        order_feed_page.wait_clickable_last_order()
        order_feed_page.click_order()
        order_feed_page.wait_for_popup_visible()
        expected_result = 'Cостав'

        assert order_feed_page.get_order_details_text() == expected_result

    @allure.title('Отображение заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    def test_view_order_on_order_feed(self, browser):
        browser.get(LOGIN_URL)
        order_feed_page = OrderFeedPage(browser)
        login_page = LoginPage(browser)

        order_feed_page.profile_login()
        login_page.create_order()
        order_id = order_feed_page.get_order_id()

        order_feed_page.goto_account()
        order_feed_page.goto_history_orders()
        order_id_history = order_feed_page.found_order_at_history(order_id)

        order_feed_page.goto_order_feed()
        order_id_order_feed = order_feed_page.found_order_at_feed(order_id)

        assert order_id_order_feed and order_id_history is True, 'Id не совпадают'

    @allure.title('Счётчик Выполнено за всё время увеличивается, при создании нового заказа')
    def test_today_orders_counter(self, browser):
        browser.get(LOGIN_URL)
        order_feed_page = OrderFeedPage(browser)
        login_page = LoginPage(browser)
        order_feed_page.profile_login()
        order_feed_page.goto_order_feed()
        pre_count = int(order_feed_page.get_total_count_today())

        order_feed_page.goto_constructor()
        login_page.create_order()
        order_feed_page.goto_order_feed()

        order_feed_page.wait_for_increased_count(TOTAL_COUNT_TODAY, pre_count)
        post_count = int(order_feed_page.get_total_count_today())
        assert post_count > pre_count, 'Счетчик не увеличился'

    @allure.title('Счётчик Выполнено за сегодня увеличивается, при создании нового заказа')
    def test_new_order_at_order_feed(self, browser):
        browser.get(LOGIN_URL)
        order_feed_page = OrderFeedPage(browser)
        login_page = LoginPage(browser)
        login_page.profile_login()
        login_page.create_order()

        order_id = order_feed_page.get_order_id()
        order_feed_page.goto_order_feed()

        assert order_feed_page.found_order_at_feed(order_id) is True
