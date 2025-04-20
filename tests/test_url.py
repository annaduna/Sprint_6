import pytest
import allure

from curl import url_dzen, url_main
from pages.main_page import MainPage


class TestUrl:
    @allure.title("Нажатие на Самокат переводит на главную страницу")
    def test_scooter_logo_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_make_order_button_top()
        main_page.click_on_scooter_logo()
        assert main_page.get_url() == url_main

    @allure.title("Нажатие на Яндекс переводит на страницу Dzen")
    def test_dzen_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        main_page.loading_wait_page_dzen(url_dzen)
        assert main_page.get_url() == url_dzen
