from selenium.webdriver.common.by import By

class MainPageLocator:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']") # Локатор для кнопки "Заказать" вверху страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")  # Локатор для кнопки "Заказать" снизу
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO=(By.XPATH, "//a[@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru']")



