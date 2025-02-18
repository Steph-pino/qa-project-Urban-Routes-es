from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Urbanroutes import UrbanRoutesPage
from localizadores import Locators


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_click_pedir_un_taxi(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_pedir_un_taxi()

    def test_choose_comfort_tariff(self):
        self.test_click_pedir_un_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_tariff()

        comfort_text = "Comfort"
        comfort_icon = routes_page.get_comfort_tarrif().text
        assert comfort_text in comfort_icon

    def test_set_phone_number(self):
        self.test_choose_comfort_tariff()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone_number(data.phone_number)

    def test_set_payment_method(self):
        self.test_set_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_payment_method_popup()
        routes_page.click_agregar_tarjeta()
        routes_page.set_card_number(data.card_number)
        assert routes_page.get_card_field().get_property('value') == data.card_number
        routes_page.set_cvv_number(data.card_code)
        routes_page.get_cvv_field().send_keys(Keys.TAB)
        routes_page.click_agregar_button()
        routes_page.close_popup_payment_method()

    def test_set_mensaje_al_conductor(self):
        self.test_set_payment_method()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_mensaje_al_conductor(data.message_for_driver)
        assert routes_page.get_mensaje_al_conductor() == data.message_for_driver

    def test_order_manta_y_panuelos(self):
        self.test_set_mensaje_al_conductor()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_manta_y_panuelos()
        #assert routes_page.get_manta_y_panuelos().get_property('checked')

    def test_order_dos_helados(self):
        self.test_order_manta_y_panuelos()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_icecream()

    def test_click_pedir_taxi_final(self):
        self.test_order_dos_helados()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_pedir_un_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


