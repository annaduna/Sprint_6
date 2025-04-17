import allure

from locators.question_locator import QuestionsLocators
from pages.base_page import BasePage
# from locators.main_page_locators import MainPageLocators
# import data


class CheckAnswer(BasePage):
    @allure.step("кликнуть на вопрос")
    def click_question(self,id):
        question_locator=QuestionsLocators.get_question_locator(id)
        self.click_on_element(question_locator)




    @allure.step('проверить текст ответа на вопрос')
    def check_answer_on_question(self, id, expected_answer):
        actual_text = self.get_text_on_element(QuestionsLocators.get_answer_locator(id))
        return actual_text == expected_answer





    @allure.step('скрол до вопроса')
    def scroll_to_question(self,id):
        question_locator= QuestionsLocators.get_question_locator(id)
        self.scroll_to_element(question_locator)

    @allure.step('подождать пока вопрос будет кликабелен')
    def wait_to_be_clic_question(self, id):
        question_locator = QuestionsLocators.get_question_locator(id)
        self.wait_for_element_to_be_clickable(question_locator)

    @allure.step('ожидание появления текста ответа на вопрос')
    def wait_answer_text(self,id):
        answer_locator = QuestionsLocators.get_answer_locator(id)
        self.wait_for_text_to_be_visible(answer_locator)




