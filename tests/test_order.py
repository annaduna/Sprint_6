import time

import pytest
import allure
from data import DataForOrder
from pages.order_details_users_page import FillingDetailsUsers
from pages.order_details_rent_page import FillingRentDetails


class TestOrder:
    @allure.title("тест на заказ самоката с двумя наборами данных")
    @pytest.mark.parametrize("user", [DataForOrder.user_1, DataForOrder.user_2])
    def test_order(self, driver, user):

        main_page = FillingDetailsUsers(driver)
        main_page.click_button_order_further()
        main_page.filling_details_users(user)
        main_page.close_cookies()
        time.sleep(1)
        main_page.click_button_next()
        page = FillingRentDetails(driver)
        page.filling_rent_details(user)

        time.sleep(10)

        # press the button Further
        # main_page.filling_form2(user1)
        # press the button Done
        # check a popup of the order confirmation
