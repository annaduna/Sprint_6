from locators.order_confirmation_locator import OrderConfirmationLocators
from pages.base_page import BasePage
import allure

class OrderConfirmationFiller(BasePage):

    @allure.step('нажать на кнопку Да')
    def click_button_yes(self):
        self.click_on_element(OrderConfirmationLocators.YES_BUTTON)





