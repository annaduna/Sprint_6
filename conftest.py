import pytest
from selenium import webdriver

from curl import url_main


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(url_main)
    yield driver
    driver.quit()