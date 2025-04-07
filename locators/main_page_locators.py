from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON_OK = (By.XPATH, "//button[@id='rcc-confirm-button']")  # Принять файлы куки
    ORDER_BUTTON_HED = (By.XPATH, "//button[@class='Button_Button__ra12g']")  # Кнопка 'Заказать' в хедере
    ORDER_BUTTON_LOW = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка 'Заказать' после блока 'Как это работает'
    LOGO_YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")  # Логотип Яндекс
    LOG0_SCOOTER_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Логотип Самокат
    BLOCK_QUESTIONS = (By.CLASS_NAME, "Home_FAQ__3uVm4")  # Блок "Вопросы о важном"

    @staticmethod
    def question_number(question):
        return By.XPATH, f'//div[@id="accordion__heading-{question}"]'  # список вопросов

    @staticmethod
    def real_text(question):
        return By.XPATH, f'//*[@id="accordion__panel-{question}"]'  # Ответ на вопрос
