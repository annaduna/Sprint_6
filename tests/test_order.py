import pytest
import allure

from curl import url_order
from data import DataForOrder
from pages.main_page import MainPage
from pages.order_confirmation_page import OrderConfirmationFiller
from pages.order_details_users_page import FillingDetailsUsers
from pages.order_details_rent_page import FillingRentDetails
from pages.order_report_page import OrderReport


class TestOrder:
    @allure.title("тест на заказ самоката с двумя наборами данных")
    @pytest.mark.parametrize("user", [DataForOrder.user_1, DataForOrder.user_2])
    def test_order(self, driver, user):
        user_info_page = FillingDetailsUsers(driver)
        user_info_page.click_button_order_header()
        user_info_page.filling_details_users(user)
        user_info_page.close_cookies()
        user_info_page.click_button_next()

        rental_details_page = FillingRentDetails(driver)
        rental_details_page.filling_rent_details(user)
        rental_details_page.click_button_make_order()

        confirmation_page = OrderConfirmationFiller(driver)
        confirmation_page.click_button_yes()

        report_page = OrderReport(driver)
        assert report_page.check_order_completion()
        report_page.click_button_check_status()
        assert report_page.check_element_txt()

    @allure.title("обе кнопки Заказ переходят на страницу заказа")
    def test_equal_order_header_footer(self, driver):
        main_page = MainPage(driver)
        main_page.click_make_order_button_top()
        top_url = main_page.get_url()
        main_page.click_on_scooter_logo()
        main_page.click_make_order_button_bottom()
        bottom_url = main_page.get_url()
        assert top_url == bottom_url
        assert top_url == url_order

