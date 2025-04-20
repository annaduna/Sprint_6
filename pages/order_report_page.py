from locators.order_report_locator import OrderReportLocators
from pages.base_page import BasePage
import allure

class OrderReport(BasePage):

    @allure.step('проверяет, что в тексте popup есть строка Заказ оформлен')
    def check_order_completion(self):
        txt = self.get_text_on_element(OrderReportLocators.REPORT_TEXT)
        return 'Заказ оформлен' in txt

    @allure.step('нажать на кнопку Посмотреть статус')
    def click_button_check_status(self):
        self.click_on_element(OrderReportLocators.CHECK_STATUS_BUTTON)






