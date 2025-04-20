from selenium.webdriver.common.by import By

class OrderReportLocators:
    REPORT_TEXT = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]") # локатор для текста
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
