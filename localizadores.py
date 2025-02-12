from selenium.webdriver.common.by import By

class Locators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_pedir_un_taxi = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_card = (By.XPATH, "//div[@class='tcard'][4]")
    phone_number_field = (By.CLASS_NAME, "np-text")

    phone_number_field_popup =(By.ID, "phone")
    Siguiente_button = (By.XPATH, "//button[text()='Siguiente']")
    codigo_sms_field = (By.XPATH, "//*[@id='code']")
# hay otro id code - pendiente revisar
    Confirmar_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_field = (By.CLASS_NAME, "pp-button filled")
    agregar_tarjeta_button = (By.CLASS_NAME, "pp-row disabled")
    card_number_field = (By.ID, "number")
    cvv_field = (By.ID, "code")
    agregar_button = (By.XPATH, "//button[text()='Agregar']")

    message_for_driver_field = (By.ID, "comment")
    manta_y_panuelos_slider = (By.XPATH, "//input[@class='switch-input'])[2]")
    plus_icecream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")