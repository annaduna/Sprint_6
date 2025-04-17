from selenium.webdriver.common.by import By

class QuestionsLocators:
    @staticmethod
    def get_question_locator(id):
        return By.XPATH, f'//*[@id="accordion__heading-{id}"]'

    @staticmethod
    def get_answer_locator(id):
        return By.XPATH, f'//*[@id="accordion__panel-{id}"]/p'
