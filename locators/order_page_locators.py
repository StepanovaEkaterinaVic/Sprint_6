from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_FIELD_STATION = (By.XPATH, "//div[text()='Лубянка']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Далее']")
    DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    RENTAL_PERIOD_2 = (By.XPATH, "//div[text()='двое суток']")
    ORDER_BUTTON_FIN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    ORDER_YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    SUCCESS_MODAL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@src='/assets/ya.svg']")
