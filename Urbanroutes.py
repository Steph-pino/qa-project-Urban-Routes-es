from localizadores import Locators
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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.comfort_card)).click()

    def set_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field)).click()
        wait.until(EC.element_to_be_clickable(Locators.phone_number_field_popup)).send_keys(phone_number)
        wait.until(EC.element_to_be_clickable(Locators.Siguiente_button)).click()

        phone_code = retrieve_phone_code(self.driver)
        wait.until(EC.element_to_be_clickable(Locators.codigo_sms_field)).send_keys(phone_code)
        wait.until(EC.element_to_be_clickable(Locators.Confirmar_button)).click()

    def open_payment_method_popup(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.payment_method_button)).click()

    def click_agregar_tarjeta(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.agregar_tarjeta_button)).click()

    def get_card_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locators.card_number_field))

    def set_card_number(self, card_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.card_number_field)).send_keys(card_number)

    def get_cvv_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locators.cvv_field))

    def set_cvv_number(self, cvv_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.cvv_field)).send_keys(cvv_number)

    def click_agregar_button(self):
        #self.driver.find_element(Locators.cvv_field).send_keys(Keys.TAB)
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.agregar_button)
        ).click()

    def close_popup_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.close_button_popup)).click()

    def set_mensaje_al_conductor(self, message):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.message_for_driver_field)).send_keys(message)

    def get_mensaje_al_conductor(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locators.message_for_driver_field)).get_attribute("value")

    def click_requisitos_pedido(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.requisitos_button)).click()

    def set_manta_y_panuelos(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.manta_y_panuelos_slider)).click()

    def set_icecream(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.plus_icecream)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(Locators.plus_icecream)).click()

    def click_pedir_un_taxi_final(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.pedir_un_taxi_last_button)).click()













