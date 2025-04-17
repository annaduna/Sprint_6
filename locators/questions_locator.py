from selenium.webdriver.common.by import By

class QuestionsLocators:
    @staticmethod
    def get_question_locator(id):
        return By.CSS_SELECTOR, f"#accordion__heading-{id}"

    @staticmethod
    def get_answer_locator(id):
        # Локатор для ответа
        return By.CSS_SELECTOR, f"#accordion__panel-{id}"
#вы хотите получить локатор для первого вопроса, вы вызываете: question_locator = QuestionsLocators.get_question_locator(0)
# Вернет (By.CSS_SELECTOR, "#accordion__heading-0")