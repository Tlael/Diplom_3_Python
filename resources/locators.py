from selenium.webdriver.common.by import By

# Общие локаторы
# Перекрывающее окно в Firefox
BUTTON_ACCOUNT_LOCATOR = (By.CSS_SELECTOR, ".AppHeader_header__link__3D_hX")

# Поле email
FIELD_EMAIL = (By.XPATH, '//label[text()="Email"]/../input')

# Поле пароль
FIELD_PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']")

# Кнопка Личный кабинет
BUTTON_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/account"]')

# Кнопка Войти
BUTTON_LOGIN = (By.XPATH, '//form/button')

# Кнопка Конструктор
BUTTON_CONSTRUCTOR = (By.XPATH, '//li/a')

# Кнопка Лента заказов
BUTTON_ORDER_FEED = (By.LINK_TEXT, 'Лента Заказов')

# Кнопка краторная булка
BUTTON_CRATOR_BUNS = (By.XPATH, '//a[img[@alt="Краторная булка N-200i"]]')

# Окно попапа с доп информацией
POPUP = (By.CSS_SELECTOR, 'div.Modal_modal__contentBox__sCy8X')

# Крестик в модальном окне Детали ингредиента
BUTTON_POPUP_CLOSED = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")

# Поле для перетаскивания ингредиентов
ADD_TO_ORDER_FIELD = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")

# Флюорисцентная булка
FLUORESCENT_BUN = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")

# Кнопка оформить заказ
CREATE_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")

# Счетчик добавления флюорисцентной булочки
COUNTER_FLUORESCENT_BUN = (By.CSS_SELECTOR, "[class='counter_counter__num__3nue1']")

# Кнопка Войти в аккаунт
BUTTON_LOGIN_IN_ACCOUNT = (By.XPATH, '//section[2]/div/button')

# Сообщение Ваш заказ начали готовить
YOUR_ORDER_MESSAGE = (By.XPATH, ".//p[contains(text(),'Ваш заказ начали готовить')]")

# Заголовок Детали ингредиента
DETAILS_ING = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")

# Локаторы login_page

# Кнопка История заказов
BUTTON_HISTORY_ORDERS = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a')

# Кнопка Выход в профиле
BUTTON_LOGOUT_IN_PROFILE = (By.XPATH, "//button[text()='Выход']")

# Локаторы order_feed_page

# Всплывающее окно с заказов
POPUP_ORDER = (By.CSS_SELECTOR, '.Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X.p-10')

# Ингредиенты последнего заказа в сплывающем окне
SEARCH_ORDER_DETAILS_TEXT = (By.XPATH, '//p[contains(@class, "text") and contains(@class, "text_type_main-medium")'
                                       ' and contains(@class, "mb-8") and text()="Cостав"]')

# Выбор последнего заказа из ленты (первый элемент массива заказов на странице)
LAST_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[1]")

# Всплывающее окно с заказом
ORDER_NUMBER_IN_INFO_WINDOW = (By.CSS_SELECTOR, ".Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X")

# Текст "идентификатор заказа"
ID_ORDER_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')

# Id оформленного заказа
ID_ORDER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

# Заказы в "История заказов"
ORDERS_AT_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                               "'text_type_digits-default')]")

# Заказы в ленте заказов
ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                            "text_type_digits-default']")

# Счетчик заказов за сегодня
TOTAL_COUNT_TODAY = (By.XPATH, '//*[text() = "Выполнено за сегодня:"]/following::*[@class][1]')

# Кнопка "Закрыть"
BUTTON_CLOSE = (By.XPATH, '//button[contains(@class,"close")]')

# Корзина заказов
BASKET_ORDER = (By.XPATH, '/html/body/div/div/main/section[2]/ul/li[2]')

# Локаторы password_recovery_page

# Кнопка Восстановить
BUTTON_RECOVERY = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

# Ссылка Восстановить пароль
LINK_RECOVERY_PASS = (By.LINK_TEXT, 'Восстановить пароль')

# Кнопка показать/скрыть пароль
BUTTON_VIEW_PASS = (By.XPATH, ".//div[contains(@class,'input__icon input__icon-action')]")

# Подсвеченное поле пароля
INPUT_PASS_FOCUSED = (By.XPATH, "//div[contains(@class, 'input_status_active')]")

PASSWORD_FIELD_PARENT = (By.XPATH, ".//input[contains(@type,'text')]/parent::div")

FIELD_NEW_PASSWORD = (By.NAME, 'Введите новый пароль')
