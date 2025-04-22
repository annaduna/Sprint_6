
from locators.order_confirmation_locator import OrderConfirmationLocators
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

    @allure.step('проверяет, что на странице статуса заказа есть элемент с текстом Посмотреть')
    def check_element_txt(self):
        txt = self.get_text_on_element(OrderConfirmationLocators.VIEW_BUTTON)
        return 'Посмотреть' in txt

    # @allure.step('дождаться смены юрл')
    # def wait_change_url_on_status_order(self):
    #     self.wait_for_url_change(self, url_order_status, timeout=10)





