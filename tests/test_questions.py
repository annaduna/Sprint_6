from pages.main_page import MainPage
import allure
from data import Questions
import pytest


class TestCheckTextAnswer:
    @allure.title("тест на проверку появления и соответствия текста ответа на вопрос")
    @pytest.mark.parametrize('order_id, expected_answer', Questions.answers)
    def test_check_text_question(self, driver, order_id, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_question(order_id)
        main_page.wait_to_be_clic_question(order_id)
        main_page.click_question(order_id)
        main_page.wait_answer_text(order_id)
        assert main_page.check_answer_on_question(order_id, expected_answer)


