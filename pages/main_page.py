import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Нажать на кнопку 'Да все привыкли")
    def agree_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON_OK)

    @allure.step("Подождать загрузки всплывающего окна cookie")
    def wait_for_agree_cookie(self):
        self.wait_for_element(MainPageLocators.COOKIE_BUTTON_OK)

    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.BLOCK_QUESTIONS)

    @allure.step("Открыть вопрос")
    def click_on_question(self, question_number):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравни ответ на вопрос")
    def check_answer_question(self, question_number, expected_text):
        answer_locator = MainPageLocators.real_text(question_number)
        self.scroll_to_element(answer_locator)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text

    @allure.step("Нажать на кнопку 'Заказать' в хедере")
    def click_on_button_hed(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HED)

    @allure.step("Нажать на кнопку 'Заказать' внизу")
    def click_on_button_low(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_LOW)








