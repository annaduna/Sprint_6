from selenium.webdriver.common.by import By

class OrderDetailsUsersLocator:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']") # Локатор для кнопки "Заказать" вверху страницы
    NEXT_BUTTON = (By.XPATH,"//button[text()='Далее']") # Локатор для кнопки "Далее"

    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']") # Локатор для поля "Имя"
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']") # Локатор для поля "Фамилия"
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # Локатор для поля "Адрес"
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Локатор для поля "Станция метро"
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # Локатор для поля "Номер телефона"



