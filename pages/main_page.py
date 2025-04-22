import allure

from locators.question_locator import QuestionsLocators
from locators.main_page_locator import MainPageLocator
from pages.base_page import BasePage



class MainPage(BasePage):
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

    @allure.step('нажатие на верхнюю кнопку Заказ')
    def click_make_order_button_top(self):
        current_url = self.driver.current_url
        self.click_on_element(MainPageLocator.ORDER_BUTTON_TOP)
        self.wait_for_url_change(current_url)

    @allure.step('нажатие на нижнюю кнопку Заказ')
    def click_make_order_button_bottom(self):
        self.scroll_to_element(MainPageLocator.ORDER_BUTTON_BOTTOM)
        current_url = self.driver.current_url
        self.click_on_element(MainPageLocator.ORDER_BUTTON_BOTTOM)
        self.wait_for_url_change(current_url)

    @allure.step('нажатие на лого Самокат')
    def click_on_scooter_logo(self):
        current_url = self.driver.current_url
        self.click_on_element(MainPageLocator.SCOOTER_LOGO)
        self.wait_for_url_change(current_url)

    @allure.step('нажатие на лого Яндекс')
    def click_on_yandex_logo(self):
        self.click_on_element(MainPageLocator.YANDEX_LOGO)

    @allure.step('ожидание загрузки страницы Dzen')
    def loading_wait_page_dzen(self, url_dzen):
        windows = self.driver.window_handles
        assert len(windows) > 1
        self.driver.switch_to.window(windows[-1])
        self.wait_for_page_load(url_dzen)  # Передача объекта driver в функцию ожидания




