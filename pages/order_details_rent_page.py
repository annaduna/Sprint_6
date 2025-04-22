from locators.order_details_rent_locator import DateRentLocators
from pages.base_page import BasePage
from data import DataRentPage
import allure

class FillingRentDetails(BasePage):

    @allure.step('нажать на кнопку Заказать')
    def click_button_make_order(self):
        self.scroll_to_element(DateRentLocators.ORDER_BUTTON)
        self.click_on_element(DateRentLocators.ORDER_BUTTON)

    @allure.step("Заполнение полей данными о заказе")
    def filling_rent_details(self, user_data):
        self.select_dropdown_no_type(DateRentLocators.RENTAL_PERIOD, user_data['time_rent']) # выбор периода заказа
        self.send_keys_to_input(DateRentLocators.RENTAL_DATE, user_data['date'])
        self.click_on_element(DataRentPage.COLOR_LOCATORS[user_data['color']])
        self.send_keys_to_input(DateRentLocators.COMMENT_FIELD, user_data['comment'])






