from selenium.webdriver.common.by import By

from locators.order_details_users_locator import OrderDetailsUsersLocator
from pages.base_page import BasePage
import allure



class FillingDetailsUsers(BasePage):

    @allure.step('нажать на кнопку "Заказать" на главной странице')
    def click_button_order_header(self):
        button_locator = OrderDetailsUsersLocator.ORDER_BUTTON_TOP
        self.click_on_element(button_locator)

    @allure.step("Заполнение полей данными про пользователя")
    def filling_details_users(self, user_data):
        self.send_keys_to_input(OrderDetailsUsersLocator.NAME_FIELD, user_data['name'])
        self.send_keys_to_input(OrderDetailsUsersLocator.LAST_NAME_FIELD, user_data['last_name'])
        self.send_keys_to_input(OrderDetailsUsersLocator.ADDRESS_FIELD, user_data['address'])
        self.select_dropdown(OrderDetailsUsersLocator.METRO_STATION_FIELD, user_data['station_metro'])
        self.send_keys_to_input(OrderDetailsUsersLocator.PHONE_NUMBER_FIELD, user_data['phone'])

    @allure.step('нажать на кнопку Далее')
    def click_button_next(self):
        self.scroll_to_element(OrderDetailsUsersLocator.NEXT_BUTTON)
        self.click_on_element(OrderDetailsUsersLocator.NEXT_BUTTON)

    @allure.step('отключить куки')
    def close_cookies(self):
        elements = self.driver.find_elements(By.XPATH, "//button[text()='да все привыкли']")
        if len(elements) > 0:
            accept_all = self.driver.find_element(By.XPATH, "//button[text()='да все привыкли']")
            accept_all.click()


