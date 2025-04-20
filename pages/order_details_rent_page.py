from locators.order_details_rent_locator import DateRentLocators
from pages.base_page import BasePage
import allure

@allure.step('Выбор локатора соответсвующего цвету из DataForOrder')
def get_color_locator(color):
    if color == 'черный жемчуг':
        return DateRentLocators.CHECKBOX_BLACK
    else:
        return DateRentLocators.CHECKBOX_GREY

class FillingRentDetails(BasePage):

    @allure.step("Заполнение полей данными о заказе")
    def filling_rent_details(self, user_data):
        self.select_dropdown_no_type(DateRentLocators.RENTAL_PERIOD, user_data['time_rent']) # выбор периода заказа
        self.send_keys_to_input(DateRentLocators.RENTAL_DATE, user_data['date'])

        color_locator = get_color_locator(user_data['color']) # выбор и клик по цветуё
        self.click_on_element(color_locator)
        self.send_keys_to_input(DateRentLocators.COMMENT_FIELD, user_data['comment'])

    @allure.step('нажать на кнопку Заказать')
    def click_button_make_order(self):
        self.scroll_to_element(DateRentLocators.ORDER_BUTTON)
        self.click_on_element(DateRentLocators.ORDER_BUTTON)





