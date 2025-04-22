import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Найти элемент, нажать на него, Выбрать из выпадающего списка")
    def select_dropdown(self, locator, value):
        element = self.driver.find_element(*locator)
        element.click()
        element.send_keys(value)
        self.driver.find_element(By.XPATH, f"//div[contains(text(), \'{value}\')]").click()

    def select_dropdown_no_type(self, locator, value):
        element = self.driver.find_element(*locator)
        element.click()
        self.driver.find_element(By.XPATH, f"//div[contains(text(), \'{value}\')]").click()
        # self.wait_for_element_to_be_clickable(locator)
        # self.click_on_element(locator)
        # self.driver.find_element(By.XPATH, f"//div[contains(text(), \'{value}\')]").click()

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать кликабельность элемента")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Подождать, пока текст элемента станет видимым")
    def wait_for_text_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('возвращает текущий url')
    def get_url(self):
        return self.driver.current_url

    @allure.step('дожидается смены url')
    def wait_for_url_change(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(url))

    @allure.step('дожидается загрузки страницы с url')
    def wait_for_page_load(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))