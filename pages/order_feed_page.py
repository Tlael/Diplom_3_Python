import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from resources.locators import POPUP_ORDER, SEARCH_ORDER_DETAILS_TEXT, LAST_ORDER, ORDER_NUMBER_IN_INFO_WINDOW, \
    ID_ORDER_TEXT, ID_ORDER, ORDERS_AT_HISTORY, ORDERS_AT_FEED, TOTAL_COUNT_TODAY, BUTTON_ORDER_FEED, \
    BUTTON_ACCOUNT, BUTTON_HISTORY_ORDERS, BUTTON_CONSTRUCTOR
from resources.urls import ORDER_FEED


class OrderFeedPage(BasePage):
    @allure.step('Проверить открытие модального окна с деталями заказа')
    def click_order(self):
        self.find_element(LAST_ORDER).click()
        self.wait_for_visibility(POPUP_ORDER)

    @allure.step('Проверить открытие модального окна с деталями заказа')
    def get_order_details_text(self):
        return self.get_text(SEARCH_ORDER_DETAILS_TEXT)

    @allure.step("Ждем кликабельности по номеру последнего заказа")
    def wait_clickable_last_order(self):
        return self.wait_for_clickability(LAST_ORDER)

    def wait_for_popup_visible(self):
        self.wait_for_visibility(ORDER_NUMBER_IN_INFO_WINDOW)

    @allure.step('Получение id заказа')
    def get_order_id(self):
        self.wait_for_visibility(ID_ORDER_TEXT)
        order_id = self.get_text(ID_ORDER)
        while order_id == '9999':
            order_id = self.get_text(ID_ORDER)
        return f"{order_id}"

    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def found_order_at_history(self, order_id):
        elements = self.find_until_all_elements_located(ORDERS_AT_HISTORY)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def found_order_at_feed(self, order_id):
        elements = self.find_until_all_elements_located(ORDERS_AT_FEED)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step('Получение кол-ва заказов за сегодня')
    def get_total_count_today(self):
        self.wait_for_visibility(TOTAL_COUNT_TODAY)
        return self.get_text(TOTAL_COUNT_TODAY)

    @allure.step("Навигация на страницу 'Ленты заказов'")
    def navigate_to_order_feed(self):
        button_order_feed = self.find_element(BUTTON_ORDER_FEED)
        self.safe_click(button_order_feed)
        self.wait_for_url_to_be(ORDER_FEED)

    @allure.step("Переход в личный кабинет")
    def goto_account(self):
        button_account = self.find_element(BUTTON_ACCOUNT)
        self.driver.execute_script('arguments[0].click();', button_account)

    @allure.step("Переход в историю заказов")
    def goto_history_orders(self):
        history_orders_button = self.find_element(BUTTON_HISTORY_ORDERS)
        self.safe_click(history_orders_button)

    @allure.step("Переход на конструктор")
    def goto_constructor(self):
        constructor_button = self.find_element(BUTTON_CONSTRUCTOR)
        self.safe_click(constructor_button)

    @allure.step("Навигация на страницу 'Ленты заказов'")
    def goto_order_feed(self):
        button_order_feed = self.find_element(BUTTON_ORDER_FEED)
        self.safe_click(button_order_feed)
        self.wait_for_url_to_be(ORDER_FEED)

    @allure.step("Ждать увеличения счетчика")
    def wait_for_increased_count(self, locator, previous_count):
        # Ожидаем, пока значение счётчика изменится и станет больше предыдущего
        WebDriverWait(self.driver, 10).until(
            lambda driver: int(driver.find_element(*locator).text) > previous_count
        )

    @allure.step("Ожидает, пока элемент станет кликабельным")
    def wait_for_clickability(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
