from selenium.webdriver.common.by import By

class DateRentLocators:
    RENTAL_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") #Локатор для поля даты аренды.
    CALENDAR_DATE_ONE = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--001']") #Локатор для первого числа (1 апреля 2025)
    CALENDAR_DATE_TWO = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--002']") #Локатор для второго числа (2 апреля 2025)
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']") #Локатор для поля срока аренды.
    SCOOTER_COLOR = (By.XPATH, "//div[text()='Цвет самоката']") #Локатор для поля цвета самоката.
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # Локатор для поля комментария.
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']") #Локатор для кнопки "Заказать".
    CHECKBOX_BLACK = (By.XPATH, "//div[@class='Order_Checkboxes__3lWSI']//label[@for='black']") #Локатор для чекбокса "чёрный жемчуг" (не нажатый)
    CHECKBOX_GREY = (By.XPATH, "//input[@id='grey']") #Локатор для чекбокса "серая безысходность", который находит элемент по атрибуту id.
    CHECKBOX_BLACK = (By.XPATH, "//input[@id='black']") #Локатор для чекбокса "чёрный жемчуг", также находит элемент по атрибуту id.