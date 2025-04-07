import allure
import pytest

import data
from pages.main_page import MainPage


class TestListImportantQuestions:
    @allure.title("Тест на проверку выпадающего списка 'Вопросы о важном'")
    @pytest.mark.parametrize('question_number, expected_text', data.Data.questions_texts)
    def test_answer_question(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        main_page.wait_for_agree_cookie()
        main_page.agree_cookie()
        main_page.wait_for_questions_list()
        main_page.click_on_question(question_number)
        assert main_page.check_answer_question(question_number, expected_text)

