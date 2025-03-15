import allure
from selenium.common import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from resources.locators import BUTTON_CONSTRUCTOR, BUTTON_ORDER_FEED, BUTTON_CRATOR_BUNS, POPUP, BUTTON_POPUP_CLOSED, \
    COUNTER_FLUORESCENT_BUN, YOUR_ORDER_MESSAGE, DETAILS_ING
from resources.urls import MAIN_PAGE, ORDER_FEED


class MainPage(BasePage):

    @allure.step("Переход на страницу конструктора")
    def go_to_constructor(self):
        button_constructor = self.find_element(BUTTON_CONSTRUCTOR)
        self.safe_click(button_constructor)
        self.wait_for_url_to_be(MAIN_PAGE)

    @allure.step("Переход на страницу ленты заказов")
    def go_to_order_feed(self):
        button_order_feed = self.find_element(BUTTON_ORDER_FEED)
        self.safe_click(button_order_feed)
        self.wait_for_url_to_be(ORDER_FEED)

    @allure.step("Открыть попап")
    def open_popup(self):
        button_crator_buns = self.find_element(BUTTON_CRATOR_BUNS)
        self.safe_click(button_crator_buns)
        self.wait_for_visibility(POPUP)

    @allure.step("Закрыть попап")
    def close_popup(self):
        button_popup_closed = self.find_element(BUTTON_POPUP_CLOSED)
        self.safe_click(button_popup_closed)

    @allure.step("Получить количество добавленных ингредиентов")
    def get_num_ingredients(self):
        counter = self.find_element(COUNTER_FLUORESCENT_BUN)
        return int(counter.text)

    @allure.step("Получить информацию о заказе")
    def get_order(self):
        return self.find_element(YOUR_ORDER_MESSAGE)

    @allure.step("Ждем, пока элемент станет невидимым")
    def wait_until_invisible(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    @allure.step("Проверяем, что элемент виден")
    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 1).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False