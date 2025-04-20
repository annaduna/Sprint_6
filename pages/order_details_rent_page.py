import time

from data import DataForOrder
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
        color_locator = get_color_locator(user_data['color']) # выбор и клик по цвету
        self.click_on_element(color_locator)

    # @allure.step("Нажимаем на чекбокс")
    # def select_checkbox(self, locator):
    #     self.click_on_element(locator)
    #     return locator.is_selected()





