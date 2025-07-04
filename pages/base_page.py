import allure
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from resources.data_user import PASSWORD, EMAIL
from resources.locators import BUTTON_ACCOUNT, BUTTON_LOGIN, FLUORESCENT_BUN, FIELD_EMAIL, FIELD_PASSWORD, \
    BUTTON_LOGIN_IN_ACCOUNT, CREATE_ORDER_BUTTON, BASKET_ORDER


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def find_element_visibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator),
                                                         message=f'Cant find element by locator {locator}')

    @allure.step("Клик по ссылке Восстановить пароль")
    def find_element(self, locator, condition=expected_conditions.presence_of_element_located, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    @allure.step("Ожидаем, пока текущий URL станет равным указанному")
    def wait_for_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    @allure.step("Ожидаем, пока элемент станет видимым")
    def wait_for_visibility(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return element

    @allure.step("Очищаем и заполняем поле значением")
    def send_keys(self, element, text):
        element.clear()
        element.send_keys(text)

    @allure.step("Возвращаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    def safe_click(self, element):
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Клик по кнопке Личный кабинет")
    def click_button_account(self):
        account_link = self.find_element(BUTTON_ACCOUNT)
        self.safe_click(account_link)

    @allure.step("Авторизация в личном кабинете")
    def profile_login(self):
        self.find_element(FIELD_EMAIL).send_keys(EMAIL)
        self.find_element(FIELD_PASSWORD).send_keys(PASSWORD)
        button_login = self.find_element(BUTTON_LOGIN)
        self.safe_click(button_login)
        self.wait_for_visibility(BUTTON_LOGIN_IN_ACCOUNT)

    @allure.step("Нажатие кнопки 'Создать заказ'")
    def click_create_order_button(self):
        create_order_button = self.find_element(CREATE_ORDER_BUTTON)
        self.safe_click(create_order_button)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        element = self.find_element_visibility(locator)
        return element.text

    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located(locator))

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)

        if self.driver.name.lower() == 'firefox':
            # Используем JavaScript для Firefox
            self.driver.execute_script("""
                function createEvent(typeOfEvent) {
                    var event = document.createEvent("CustomEvent");
                    event.initCustomEvent(typeOfEvent, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(key, value) {
                            this.data[key] = value;
                        },
                        getData: function(key) {
                            return this.data[key];
                        }
                    };
                    return event;
                }

                // Начинаем процесс перетаскивания
                var event = createEvent('dragstart');
                arguments[0].dispatchEvent(event);

                // Завершаем процесс перетаскивания
                var dropEvent = createEvent('drop');
                arguments[1].dispatchEvent(dropEvent);
            """, draggable, droppable)
        else:
            # Используем стандартные ActionChains для остальных браузеров
            ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    @allure.step('Перетаскивание ингредиента')
    def add_filling_to_order(self):
        self.find_element_clickable(FLUORESCENT_BUN)
        self.drag_and_drop_on_element(FLUORESCENT_BUN, BASKET_ORDER)

    def find_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")
