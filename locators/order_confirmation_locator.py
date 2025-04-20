from selenium.webdriver.common.by import By

class OrderConfirmationLocators:
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]") # локатор для кнопки Да в окне подтверждения заказа
