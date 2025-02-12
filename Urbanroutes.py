from localizadores import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import data
from selenium.webdriver.common.keys import Keys

def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*Locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*Locators.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_pedir_un_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.button_pedir_un_taxi)).click()

    def set_comfort_tariff(self):
        self.driver.find_element(Locators.comfort_card).click()
        WebDriverWait(self.driver, 10)

    def set_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.phone_number_field)).click()
        self.driver.find_element(Locators.phone_number_field_popup).send_keys(phone_number)
        wait.until(EC.element_to_be_clickable(Locators.Siguiente_button)).click()

        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(Locators.codigo_sms_field).send_keys(phone_code)
        wait.until(EC.element_to_be_clickable(Locators.Confirmar_button)).click()


    def get_card_field(self):
        return self.driver.find_element(Locators.card_number_field)

    def set_card_number(self, card_number):
        self.get_card_field().send_keys(card_number)

    def get_cvv_field(self):
        return self.driver.find_element(Locators.cvv_field)

    def set_cvv_number(self, cvv_number):
        self.get_cvv_field().send_keys(cvv_number)

    def set_agregar_button(self):
        self.driver.find_element(Locators.cvv_field).send_keys(Keys.TAB)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.agregar_button)).click()

    def open_add_payment_method_popup(self):
        self.driver.find_element(Locators.payment_method_field).click()

    def set_payment_method(self, card_number, cvv_number):
        self.open_add_payment_method_popup()
        self.set_card_number(card_number)
        current_card_number = self.get_card_field().get_property('value')
        assert data.card_number == current_card_number
        self.set_cvv_number(cvv_number)
        self.set_agregar_button()

    def set_mensaje_al_conductor(self, message):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.message_for_driver_field)).send_keys(message)

    def set_manta_y_pañuelos(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.manta_y_panuelos_slider)).click()

    def set_icecream(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.plus_icecream)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.plus_icecream)).click()











