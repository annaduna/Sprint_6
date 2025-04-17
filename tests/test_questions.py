from pages.main_page import CheckAnswer
import allure
from data import Questions
import pytest


class TestCheckTextAnswer:
    @allure.title("тест на проверку появления и соответствия текста ответа на вопрос")
    @pytest.mark.parametrize('id, expected_answer', Questions.answers)
    def test_check_text_question(self, driver, id, expected_answer):
        main_page = CheckAnswer(driver)
        main_page.scroll_to_question(id)
        main_page.wait_to_be_clic_question(id)
        main_page.click_question(id)
        main_page.wait_answer_text(id)
        assert main_page.check_answer_on_question(id, expected_answer)


