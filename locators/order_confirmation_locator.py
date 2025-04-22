from selenium.webdriver.common.by import By

class OrderConfirmationLocators:
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]") # локатор для кнопки Да в окне подтверждения заказа
    VIEW_BUTTON = (By.XPATH,"//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Посмотреть')]")

